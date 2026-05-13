---
name: deploy-staging
description: Enseña a Pi a desplegar en staging usando Docker Compose. Se activa cuando el usuario pide desplegar, hacer deploy, o subir a staging.
---

# Deploy Staging

Skill para desplegar servicios en entorno de staging con Docker Compose.

## Requisitos previos
- Docker y Docker Compose instalados
- Archivo `docker-compose.yml` (o `docker-compose.staging.yml`) en el proyecto

## Workflow

### 1. Verificar entorno
Confirmar que no hay servicios conflictivos ya corriendo:

```bash
docker compose ps
```

### 2. Build
Construir las imágenes sin cache:

```bash
docker compose build --no-cache
```

### 3. Deploy
Levantar los servicios en modo detached:

```bash
docker compose up -d
```

Si existe un compose específico de staging, usarlo:

```bash
docker compose -f docker-compose.staging.yml up -d
```

### 4. Verificar despliegue
Revisar que los servicios arrancaron correctamente:

```bash
docker compose logs --tail=30
docker compose ps
```

### 5. Health check (opcional)
Si el proyecto expone un endpoint de salud:

```bash
curl -s http://localhost:8080/health || echo "Health check falló"
```
