# Prototipo de detector de patentes para control de acceso

Prototipo de reconocimiento automático de patentes vehiculares sobre un video de prueba, con detección YOLO y lectura de texto por OCR.

![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=flat&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Estado](https://img.shields.io/badge/estado-terminado-blue?style=flat)
![Licencia](https://img.shields.io/badge/licencia-AGPL--3.0-blue?style=flat)
![Último commit](https://img.shields.io/github/last-commit/ViceAguilera/detector-script-demo?style=flat)

<!-- Demo: agrega una captura o GIF en docs/demo.gif y descomenta la línea siguiente -->
<!-- <p align="center"><img src="docs/demo.gif" alt="Demostración del prototipo de detector de patentes" width="800"></p> -->

## Tabla de contenidos

- [Descripción](#descripción)
- [Estado del proyecto](#estado-del-proyecto)
- [Características](#características)
- [Tecnologías](#tecnologías)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Contribuir](#contribuir)
- [Licencia](#licencia)
- [Autores](#autores)

## Descripción

Primera versión (0.3.0 beta) del detector de patentes que dio origen a un proyecto de tesis de control de acceso. Procesa un video, localiza las patentes con un modelo YOLO propio, las lee con EasyOCR y envía cada lectura a una API HTTP. Se desarrolló en colaboración con Camilo Sáez Garrido, quien construyó la API. La versión posterior está en [detector-script-tesis](https://github.com/ViceAguilera/detector-script-tesis).

## Estado del proyecto

**Terminado.** Primera versión (0.3.0 beta), reemplazada por detector-script-tesis; no recibe mantenimiento activo.

## Características

- Detección de patentes con un modelo YOLO (`app/model/licence_plate.pt`).
- Lectura del texto con EasyOCR sobre la imagen en escala de grises y binarizada.
- Validación del texto: entre 6 y 9 caracteres alfanuméricos, confianza mínima de 0.7 y no compuesto solo por letras.
- Omite lecturas consecutivas idénticas.
- Envío del resultado (patente, confianza y nombre de imagen) por POST a `/api/registers` del servidor configurado.
- Ejecución local con entorno virtual o en contenedor Docker.

## Tecnologías

- Python 3.9
- [Ultralytics](https://ultralytics.com/) (YOLO)
- [OpenCV](https://opencv.org/)
- [EasyOCR](https://www.jaided.ai/easyocr/)
- python-dotenv
- Docker

## Requisitos

- Git
- Docker (entorno de desarrollo original: Docker 23.0.5 sobre Windows 10), o bien Python 3.9 con `venv` en Linux
- Un servidor con la API de registros, cuyo host y puerto se definen en `app/.env`

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/ViceAguilera/detector-script-demo.git
cd detector-script-demo
```

Configura las variables de entorno en `app/` (renombra `.env.example` a `.env` y completa `HOST` y `PORT`):

```
HOST=
PORT=
```

### Con Docker

```bash
docker build -t detector-script .
docker run --name detector-script detector-script
```

### Sin Docker (Linux)

```bash
sudo apt-get install python3.9-venv
sudo apt-get update && sudo apt-get install -y libgl1-mesa-glx
python3.9 -m venv venv
source venv/bin/activate
cd app
pip install -r requirements.txt
# El proyecto original usa una versión anterior de Pillow
pip uninstall -y Pillow
pip install Pillow==9.0.1
```

## Uso

```bash
cd app
python3.9 main.py
```

El script lee `app/video/test.mp4` y, por cada patente detectada, imprime el texto y la confianza y la envía a la API.

## Estructura del proyecto

```
app/
├── main.py            # Detección, OCR y envío a la API
├── model/             # Modelo de patentes (licence_plate.pt)
├── video/test.mp4     # Video de prueba
├── requirements.txt   # Dependencias
└── .env.example       # Plantilla de variables de entorno
Dockerfile             # Imagen del contenedor
CONTRIBUTING.md        # Guía de contribución
```

## Contribuir

Revisa la [guía de contribución](CONTRIBUTING.md).

## Licencia

Distribuido bajo la licencia GNU AGPL-3.0. Ver [LICENSE](LICENSE).

## Autores

**Vicente Aguilera Arias** — [Portafolio](https://portfolio.iamsirius.cl) · [GitHub](https://github.com/ViceAguilera) · [LinkedIn](https://www.linkedin.com/in/vicenteaguilera/)

Colaborador: [Camilo Sáez Garrido](https://github.com/camjasaez) (API)
