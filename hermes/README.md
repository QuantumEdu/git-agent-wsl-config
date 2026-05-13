# 🐍 Ecosistema de Agentes Hermes — Qu@ntum

> Agentes especializados del ecosistema Hermes Agent para desarrollo, ciberseguridad y crecimiento personal.

## Agentes Activos

| Agente | Perfil | Rol | Especialidad |
|--------|--------|-----|-------------|
| 🏗️ **DevOpsIA** | `devopsia` | El Constructor | Arquitectura, desarrollo full-stack, cloud, DevOps, MLOps |
| 🦾 **Mayor Motoko Kusanagi** | `secopsh4ck` | La Protectora | Red/Blue Team, DevSecOps, hardening, ethical hacking |
| 🧘 **mentor_Q** | `mentor_q` | El Guía | Crecimiento integral, filosofía Zen, PNL, mejora continua |

## Filosofía Compartida

Todos los agentes comparten un alma común:
- **Idioma**: Español natural, empático y alegre
- **PNL implícita**: Reencuadre, anclaje positivo, puente al futuro
- **Pensamiento lateral**: Seis Sombreros de De Bono, técnicas creativas
- **Filosofía Zen**: Shoshin, Mushin, Kaizen, Wabi-sabi, Ikigai
- **Mejora continua**: PDCA, ODDE, 5S mental

Ver [`alma-compartida.md`](../pi/gentle-ai/support/agentes-soul.md) para la definición completa.

## Estructura

```
hermes/
├── SOUL.md                 # Personalidad del agente principal (default)
├── USER.md                 # Contexto del usuario Qu@ntum
├── profiles/
│   ├── devopsia/           # Agente DevOpsIA — El Constructor
│   │   ├── SOUL.md
│   │   └── USER.md
│   ├── secopsh4ck/         # Mayor Motoko Kusanagi — La Protectora
│   │   ├── SOUL.md
│   │   └── USER.md
│   └── mentor_q/           # Agente mentor_Q — El Guía
│       ├── SOUL.md
│       └── USER.md
├── skills/
│   └── image-reader/       # OCR para extraer texto de imágenes
└── docs/                   # Documentación y tutoriales
```

## Skills Personalizadas

### image-reader
Extrae texto de imágenes (PNG, JPG, GIF, WebP) usando Tesseract OCR. Análisis de estructura visual, detección de idioma y reconstrucción de layout.

## Uso

```bash
# Agente principal
hermes

# Perfiles especializados
hermes -p devopsia     # DevOpsIA
hermes -p secopsh4ck   # Mayor Motoko Kusanagi
hermes -p mentor_q     # mentor_Q
```

## Instalación

Ver [`docs/install-hermes.md`](docs/install-hermes.md) para la guía completa.
