# Proyecto Taller de desarrollo

###### **Universidad del Bío-Bío**

_Sistema de reconocimiento automático de matrículas vehiculares y API para el control de acceso en tiempo real_

### Paso a paso para la instalación del proyecto
- Se actualiza el sistema operativo.
```
$ apt-get update -y && apt-get upgrade -y
```
- Se instala el python 3.9, pip, venv y git.
```
$ apt install -y python3.9 python3-pip python3.9-venv git
```
- Se clona el repositorio.
```
$ git clone https://github.com/ViceAguilera/detector-script-tesis.git detector-script
```
- Se ingresa a la carpeta del proyecto.
```
$ cd detector-script
```
- Se crea el entorno virtual.
```
$ python3.9 -m venv venv
```
- Se activa el entorno virtual.
```
$ source venv/bin/activate
```
- Se instalan las librerias.
```
$ pip install -r requirements.txt
```
- Se ejecuta el script.
```
$ python3.9 main.py
```

