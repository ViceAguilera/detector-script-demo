# Prototipo de detector de patentes para el control de acceso en tiempo real

###### **🚧 V0.3.0 Beta development.🚧🔨**

_Sistema de reconocimiento automático de matrículas vehiculares y API para el control de acceso en tiempo real_

## Construido con 🛠️

- [Python v3.9](https://www.python.org/) - Lenguaje de programación

### Pre-requisitos de desarrollo 📋

Para poder ejecutar el proyecto se necesita tener instalado:

- [Git](https://git-scm.com/downloads) - Control de versiones de código
- [Docker](https://docs.docker.com/get-docker/) - Contenedores de aplicaciones para el desarrollo y despliegue de software

_❗Se debe cambiar la variable de entorno dentro del archivo .env.example a la variable de entorno de la maquina_

_El entorno de desarrollo utilizado fue Windows 10 Version 22H2 (OS Build 19045.3208)_

### Configuraciones de ejecución para entorno de desarrollo

#### Instalacion

- Para instalar el proyecto se debe clonar el repositorio y nos posicionamos en la carpeta del proyecto.

  ```bash
  git clone https://github.com/ViceAguilera/detector-script-tesis.git detector-script
  cd detector-script
  ```
  
- Luego se debe construir la imagen de Docker

  ```bash
  docker build -t detector-script .
  ```

- Despues se debe ejecutar el contenedor de Docker
  ```bash
  docker run -v "$(pwd)\app:\app" --name detector-script detector-script
  ```

_La versión de Docker utilizada para desarrollo fue 23.0.5, build bc4487a_

### Pre-requisitos de produccion 📋

Para poder ejecutar el proyecto se necesita tener instalado:

- [Ubuntu](https://ubuntu.com/download) - Control de versiones de código
- [Git](https://git-scm.com/downloads) - Contenedores de aplicaciones para el desarrollo y despliegue de software

_❗Se debe cambiar la variable de entorno dentro del archivo .env.example a la variable de entorno de la maquina_


### Configuraciones de ejecución para entorno de produccion

#### Instalacion

- Se debe instalar venv
  ```bash
  sudo apt-get install python3.9-venv
  ```
  
- Se debe instalar un packete para OpenCV
  ```bash
  sudo apt-get update && apt-get install -y libgl1-mesa-glx
  ```

- Se clona el repositorio de GitHub
  ```bash
  git clone https://github.com/ViceAguilera/detector-script-tesis.git detector-script
  ```
  
- Se ingresa a la carpeta del proyecto
  ```bash
  cd detector-script
  ```
  
- Se crea un entorno virtual
  ```bash
  python3.9 -m venv venv
  ```
  
- Se activa el entorno virtual
  ```bash
  source venv/bin/activate
  ```
  
- Se ingresa a la carpeta app
  ```bash
  cd app
  ```

- Se instala los requerimientos del proyecto
  ```bash
  pip install -r requirements.txt
  ```

- Se desinstala la libreria Pillow 10.0.0
  ```bash
  pip uninstall -y Pillow
  ```

- Se instala una version anterior de Pillow
  ```bash
  pip install Pillow==9.0.1
  ```

- Se agregan el nombre al archivo .env.example
  ```bash
  mv .env.example .env
  ```

- Se le cambian las variables de entorno HOST y PORT al archivo .env
  ```bash
  nano .env
  ```

- Se ejecuta el script
  ```bash
  python3.9 main.py
  ```

## Construido con 
- [OpenCV](https://opencv.org/) - Librería de visión artificial
- [Easy OCR](https://www.jaided.ai/easyocr/) - Librería de reconocimiento óptico de caracteres
- [Ultralytics](https://ultralytics.com/) - Librería de modelo de detección de objetos

## Licencia 📄

Este proyecto está bajo la GNU Affero General Public License v3.0 - mira el archivo [LICENSE](LICENSE) para detalles

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](CONTRIBUTING.md) para mas detalles.