# AGENTS.md

OCR web app — Flask + Tesseract, en Docker.

## Estructura

```
Ocr/
├── app/
│   ├── main.py           # Servidor Flask, rutas GET / y POST /ocr
│   ├── static/
│   │   └── favicon.svg   # Favicon SVG (documento con líneas de texto)
│   └── templates/
│       └── index.html    # Frontend: selector archivo, preview, botón OCR, textarea resultado
├── docker-compose.example.yml   # Ejemplo público (sin datos personales)
├── docker-compose.yml           # Ignorado por git (personal)
├── Dockerfile
├── requirements.txt
├── .gitignore
└── AGENTS.md
```

## Comandos

```bash
# Construir y ejecutar
docker compose up -d

# Reconstruir sin caché
docker compose build --no-cache && docker compose up -d

# Abrir en navegador
# http://localhost:5010
```

## Detalles importantes

- **OCR**: usa `pytesseract` con idioma `spa+eng` (español + inglés)
- **Dependencia sistema**: requiere `tesseract-ocr` y `tesseract-ocr-spa` (ya instalados en el Dockerfile)
- **Puerto**: 5010 (configurado en `main.py` y expuesto en Dockerfile)
- **Producción**: usa `gunicorn` como WSGI (no el servidor dev de Flask).
- **Frontend**: HTML plano + JS vanilla, sin frameworks. Drag & drop + selección de archivo. Zoom y recorte con cropperjs (CDN). Modos toggle: "Recortar" (mover/redimensionar recuadro) y "Mover" (desplazar imagen con zoom).
- **Debug**: ya no se usa `debug=True` (desactivado).
