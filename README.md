# OCR Web App

Aplicación web para reconocimiento de texto en imágenes (OCR) usando Tesseract.

Carga una imagen, selecciona el área de interés con recorte y zoom, y obtén el texto extraído al instante.

## Stack

- **Backend**: Flask + Gunicorn
- **OCR**: Tesseract (español + inglés)
- **Frontend**: HTML plano + cropperjs (CDN)
- **Contenedor**: Docker

## Uso rápido

```bash
docker compose up -d
# Abrir http://localhost:5010
```

## Funcionalidades

- Carga de imagen por drag & drop o selector de archivos
- Zoom y recorte del área a procesar
- Modos toggle: Recortar (ajustar selección) / Mover (desplazar imagen)
- OCR en español e inglés
- Responsive (funciona en móvil)

## Estructura

```
├── app/
│   ├── main.py            # Servidor Flask
│   ├── static/favicon.svg
│   └── templates/index.html
├── Dockerfile
├── docker-compose.example.yml
└── requirements.txt
```
