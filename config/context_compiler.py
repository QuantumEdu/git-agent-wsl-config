#!/usr/bin/env python3
import os
import sqlite3
import re
from datetime import datetime

quantum_dir = "/home/hermes/.quantum-os"
db_path = "/home/hermes/.engram/engram.db"

def compile_context():
    if not os.path.exists(db_path):
        print(f"[ERROR] No se encontró la base de datos de Engram en {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("[INFO] Iniciando compilación de contexto desde Engram a ~/.quantum-os/...")

    # 1. Recuperar observaciones / hechos recientes
    # Verificamos si la tabla observaciones existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='observations'")
    has_observations = cursor.fetchone() is not None

    recent_preferences = []
    project_preferences = {}
    recent_life_context = []
    project_updates = {}

    if has_observations:
        # Traer las observaciones activas y no borradas, ordenadas por actualización
        cursor.execute("""
            SELECT type, title, content, project, updated_at 
            FROM observations 
            WHERE deleted_at IS NULL
            ORDER BY updated_at DESC
        """)
        observations = cursor.fetchall()

        for obs in observations:
            o_type, o_title, o_content, o_project, o_updated = obs
            o_project = o_project if o_project else "global"
            
            # Clasificar por tipo/destino
            if o_type in ['preference', 'interaction_rule', 'rule']:
                pref_str = f"- **{o_title}**: {o_content} *(Actualizado: {o_updated})*"
                if o_project == "global":
                    recent_preferences.append(pref_str)
                else:
                    if o_project not in project_preferences:
                        project_preferences[o_project] = []
                    project_preferences[o_project].append(pref_str)
            elif o_type in ['life_context', 'goal', 'habit', 'personal']:
                recent_life_context.append(f"- **{o_title}**: {o_content} *(Actualizado: {o_updated})*")
            elif o_type in ['bugfix', 'discovery', 'decision', 'session_summary']:
                if o_project not in project_updates:
                    project_updates[o_project] = []
                project_updates[o_project].append({
                    'type': o_type,
                    'title': o_title,
                    'content': o_content,
                    'date': o_updated
                })

    # 2. Actualizar AGENT_RULES.md (Nivel 1)
    agent_rules_path = os.path.join(quantum_dir, "identity/AGENT_RULES.md")
    rules_header = """# AGENT_RULES.md - Reglas de interacción para todos los agentes AI

## Identidad y Roles
- Eres el asistente inteligente de **Quantum (Dr. Gabriel Magallón)**.
- Te organizas con el método **PARA + ACE** dentro de `/home/hermes/para_ace/`.

## Lineamientos de Comunicación
- Sé conciso, directo y técnico. No agregues cortesías innecesarias o introducciones largas.
- Usa renderizado de texto simple para terminal cuando estés en la CLI.
- No generes etiquetas de tipo `MEDIA:/path` si estás operando directamente en un entorno CLI.
"""
    if recent_preferences:
        rules_header += "\n## Reglas Dinámicas Detectadas (Sincronizadas desde Engram)\n"
        rules_header += "\n".join(recent_preferences[:10])  # Limitar a las 10 más recientes para budget de tokens
        rules_header += "\n"

    with open(agent_rules_path, "w") as f:
        f.write(rules_header)
    print("[SUCCESS] AGENT_RULES.md actualizado.")

    # 3. Actualizar LIFE_CONTEXT.md (Nivel 1 - Alimentado por Pi Agent)
    life_context_path = os.path.join(quantum_dir, "identity/LIFE_CONTEXT.md")
    life_header = """# LIFE_CONTEXT.md - Contexto de Vida y Objetivos (Sincronizado desde Pi/Acompañamiento)

## Enfoque de Vida
- Dr. Gabriel Magallón (Quantum).
- Enfoque en educación de vanguardia (QuantumEdu), automatización AI, desarrollo ágil y mentoría.
- Balance entre vida profesional, salud y coaching.
"""
    if recent_life_context:
        life_header += "\n## Actualizaciones de Pi y Metas Personales\n"
        life_header += "\n".join(recent_life_context[:10])
        life_header += "\n"

    with open(life_context_path, "w") as f:
        f.write(life_header)
    print("[SUCCESS] LIFE_CONTEXT.md actualizado.")

    # 4. Actualizar Proyectos Activos (Nivel 2 y 3)
    for project, updates in project_updates.items():
        if project == "global":
            continue
            
        proj_dir = os.path.join(quantum_dir, "projects", project)
        if not os.path.exists(proj_dir):
            os.makedirs(proj_dir, exist_ok=True)
            print(f"[INFO] Nueva carpeta de proyecto creada para: {project}")

        # Actualizar DECISIONS.md (Nivel 3)
        decisions_path = os.path.join(proj_dir, "DECISIONS.md")
        decisions_content = f"# DECISIONS.md - Decisiones del Proyecto {project.title()}\n\n"
        decisions_content += "## Registro Automático de Decisiones y Logros (Desde Engram)\n\n"
        
        for item in updates:
            decisions_content += f"### [{item['date']}] {item['title']} ({item['type'].upper()})\n"
            decisions_content += f"- **Detalle:** {item['content']}\n\n"
            decisions_content += "---\n\n"

        with open(decisions_path, "w") as f:
            f.write(decisions_content)
        print(f"[SUCCESS] DECISIONS.md actualizado para {project}.")

        # Actualizar CONTEXT.md (Nivel 2 - Mantener TL;DR limpio)
        context_path = os.path.join(proj_dir, "CONTEXT.md")
        
        # Intentamos preservar el TL;DR si ya existía el archivo
        tldr_section = f"""## TL;DR [~80 tokens — SIEMPRE leer esto]
Estado: Desarrollo activo (Sincronizado).
Proyecto: {project.title()}
Siguiente: Consultar DECISIONS.md para el log completo de avances.
Bloqueador: Ninguno."""

        if os.path.exists(context_path):
            with open(context_path, "r") as f:
                content = f.read()
            match = re.search(r"## TL;DR.*?(?=\n---|\\Z)", content, re.DOTALL)
            if match:
                tldr_section = match.group(0).strip()

        # Construir nuevo CONTEXT.md combinando el TL;DR con los últimos 3 logros de Engram
        new_context = f"# CONTEXT.md - {project.title()}\n\n"
        new_context += tldr_section + "\n\n---\n\n## Detalle Completo [~800 tokens — leer solo si preguntan]\n\n"
        new_context += "### Avances Recientes Sincronizados:\n"
        
        # Agregar los 3 updates más recientes para no inflar tokens
        for item in updates[:3]:
            new_context += f"- **[{item['type'].upper()}] {item['title']}**: {item['content'][:150]}...\n"
            
        with open(context_path, "w") as f:
            f.write(new_context)
        print(f"[SUCCESS] CONTEXT.md compilado para {project}.")

        # 5. Generar .cursorrules para el proyecto
        cursorrules_path = os.path.join(proj_dir, ".cursorrules")
        
        # Combinar preferencias globales y del proyecto
        combined_rules = []
        combined_rules.extend(recent_preferences[:10])
        if project in project_preferences:
            combined_rules.extend(project_preferences[project][:10])
            
        cursorrules_content = f"""# .cursorrules - Configuración de Cursor para {project.title()}

## Directrices del Proyecto
- Carpeta del Proyecto: `/home/hermes/.quantum-os/projects/{project}`
- Organización: Método PARA + ACE dentro de `/home/hermes/para_ace/`
- Respuestas directas, técnicas y concisas. Sin saludos ni formalidades innecesarias.

## Reglas de Codificación e Interacción
- Utilizar siempre rutas absolutas para operaciones del sistema de archivos.
- Verificar archivos existentes con herramientas de lectura antes de editar o escribir de cero.
- Realizar llamadas a herramientas en paralelo siempre que sea posible.
- Evitar etiquetas decorativas estilo `MEDIA:/path` si estás operando directamente en CLI.

"""
        if combined_rules:
            cursorrules_content += "## Reglas Dinámicas Recientes (Desde Engram)\n"
            cursorrules_content += "\n".join(combined_rules[:15]) + "\n\n"
            
        cursorrules_content += f"""## Instrucciones Específicas
- Para cambios importantes, registrar decisiones en `DECISIONS.md`.
- Mantener la sección TL;DR en `CONTEXT.md` siempre actualizada y concisa.
"""
        with open(cursorrules_path, "w") as f:
            f.write(cursorrules_content)
        print(f"[SUCCESS] .cursorrules generado para {project}.")

        # 6. Generar CLAUDE.md para el proyecto
        claude_path = os.path.join(proj_dir, "CLAUDE.md")
        
        # Intentamos deducir comandos básicos o mantener un estándar robusto
        claude_content = f"""# CLAUDE.md - Guía de Desarrollo para Claude en {project.title()}

Este archivo define comandos de compilación/test e instrucciones de estilo para el proyecto {project.title()}.

## Comandos de Desarrollo Comunes
- No hay comandos automáticos de compilación para este proyecto. Utilizar scripts en el directorio si existen.
- Para verificar sintaxis de Python (si aplica): `python3 -m py_compile *.py`

## Reglas de Estilo e Instrucciones
1. **Comportamiento General**: Sé extremadamente conciso, técnico y directo.
2. **Sistema de Archivos**: Siempre usa rutas absolutas en lugar de relativas.
3. **Manejo de Errores**: Robustez primero. Si faltan recursos u observaciones, maneja el caso de manera segura y silenciosa o informando con [INFO]/[WARNING] sin lanzar excepciones.
4. **Sincronización**: Mantener el contexto sincronizado a través de los archivos del proyecto (`CONTEXT.md`, `DECISIONS.md`).
"""
        with open(claude_path, "w") as f:
            f.write(claude_content)
        print(f"[SUCCESS] CLAUDE.md generado para {project}.")

    conn.close()
    print("[INFO] Sincronización de contexto completada con éxito.")

    # Sincronización con el repositorio git-agent-wsl-config
    git_repo_path = "/home/hermes/git-agent-wsl-config"
    if os.path.exists(git_repo_path):
        print("[INFO] Sincronizando compilación con git-agent-wsl-config...")
        import subprocess
        try:
            # Copiar los archivos compilados al repo
            subprocess.run(f"cp -r {quantum_dir}/identity {git_repo_path}/config/", shell=True, check=True)
            subprocess.run(f"cp -r {quantum_dir}/projects {git_repo_path}/config/", shell=True, check=True)
            subprocess.run(f"cp -r {quantum_dir}/knowledge {git_repo_path}/config/", shell=True, check=True)
            subprocess.run(f"cp {quantum_dir}/context_compiler.py {git_repo_path}/config/", shell=True, check=True)
            
            # Verificar cambios en el git repo
            status_res = subprocess.run(["git", "-C", git_repo_path, "status", "--porcelain"], capture_output=True, text=True, check=True)
            if status_res.stdout.strip():
                print("[INFO] Cambios significativos detectados. Realizando commit...")
                subprocess.run(["git", "-C", git_repo_path, "add", "config/identity", "config/projects", "config/knowledge", "config/context_compiler.py"], check=True)
                subprocess.run(["git", "-C", git_repo_path, "commit", "-m", "chore: updates compiled from engram"], check=True)
                print("[SUCCESS] Commit realizado en git-agent-wsl-config.")
            else:
                print("[INFO] No se detectaron cambios significativos para realizar commit.")
        except Exception as e:
            print(f"[ERROR] Error durante la sincronización git: {e}")


if __name__ == "__main__":
    compile_context()
