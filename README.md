# Prototipo de detector de patentes para el control de acceso en tiempo real

###### **🚧 V0.3.0 Beta development.🚧🔨**

_Sistema de reconocimiento automático de matrículas vehiculares y API para el control de acceso en tiempo real_

## Construido con 🛠️

- [Python v3.9](https://www.python.org/) - Lenguaje de programación
- [MongoDB Atlas](https://www.mongodb.com/atlas/database) - Base de datos NoSQL en la nube
- [FastAPI v0.97](https://fastapi.tiangolo.com/) - Framework para API
- [OpenCV](https://opencv.org/) - Librería de visión artificial
- [Easy OCR](https://www.jaided.ai/easyocr/) - Librería de reconocimiento óptico de caracteres
- [Ultralytics](https://ultralytics.com/) - Librería de modelo de detección de objetos
- [Supervision](https://github.com/roboflow/supervision) - Libreria para cargar detecciones de video.

### Pre-requisitos 📋

Para poder ejecutar el proyecto se necesita tener instalado:

- [Git](https://git-scm.com/downloads) - Control de versiones de código
- [Docker](https://docs.docker.com/get-docker/) - Contenedores de aplicaciones para el desarrollo y despliegue de software

_El entorno de desarrollo utilizado fue Windows 10 Version 22H2 (OS Build 19045.3208)_

### Instalación y configuracion 🔧

#### Configuracion inicial

- Para poder ejecutar el proyecto se debe crear un archivo `.env` en la carpeta `app/config` con las variables de entorno según el archivo `.env.example`.

#### Instalacion

- Para instalar el proyecto se debe clonar el repositorio y nos posicionamos en la carpeta del proyecto.

  ```
  git clone <link> detector-script
  cd detector-script
  ```
  
- Luego se debe construir la imagen de Docker

  ```bash
  docker build -t detector-script .
  ```

- Despues se debe ejecutar el contenedor de Docker
  ```bash
  docker run -p 8000:8000 -v "$(pwd)/app:/app" --name detector-script detector-script
  ```

_La versión de Docker utilizada para desarrollo fue 23.0.5, build bc4487a_

## Licencia 📄

Este proyecto está bajo la Licencia X - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](CONTRIBUTING.md) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Autores ✒️

[**Camilo Sáez Garrido**](https://github.com/camjasaez) & [**Vicente Aguilera Arias**](https://github.com/ViceAguilera)