# Guia de contribución

### Autores

- Vicente Aguilera Arias - Desarrollo de Script detector - vicente.aguilera2001@alumnos.ubiobio.cl
- Camilo Sáez Garrido - Desarrollo de la API - camilo.saez1601@alumnos.ubiobio.cl

### Estandares de codificación

El estilo de codificación de Python se basa en [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

### Configuracion de editor de codigo

Se recomienda utilizar el editor de código [Pycharm](https://www.jetbrains.com/es-es/pycharm/download/?section=windows).

Configuraciones generales:

- Saltos de linea: LF
- Codificación de archivo: UTF-8
- Tamaño de tabulación: 4

### Desarrollo de codigo

#### Estilo de codigo y convenciones

- El codigo esta escrito en ingles.
- Los nombres de las variables, funciones se escriben en minusculas y separadas por guiones bajos. Utilizando `snake_case`.

#### Estructura de carpetas

El codigo se debe desarrollar en la carpeta `app` y se debe seguir la siguiente estructura:

```
app
├── model
│   ├── licence_plate.pt
│   └── ...
├── video
│   ├── sample.mp4
│   └── ...
├── main.py
└── requirements.txt
```

- Esta estructura de carpetas sigue un enfoque basado en tipo de archivo (File type-based structure), esta estructura organiza las carpetas en función del tipo de archivo.
- Este detector sigue la siguiente estructura:
  - `model`: Contiene el modelo.
    - `licence_plate.pt`: Modelo de licencias de vehiculos.
  - `video`: Contiene los archivos multimedia.
    - `sample.mp4`: Video de prueba.
  - `main.py`: Archivo principal de la aplicación.
  - `requirements.txt`: Archivo de dependencias de la aplicación.

### Interaccion con el repositorio

#### Ramas de git

- La rama principal es `main`, esta rama contiene el código estable y funcional.
- La rama `develop` es la rama de desarrollo, esta rama contiene el código en desarrollo de futuras versiones y no es estable.
- Las ramas de desarrollo de nuevas funcionalidades se crean a partir de la rama `develop` y se nombran con el prefijo `feature/` seguido del nombre de la funcionalidad.
- Las ramas de desarrollo de corrección de errores se crean a partir de la rama `develop` y se nombran con el prefijo `bugfix/` seguido del nombre del error.
- Una vez finalizada la funcionalidad o corrección de errores se debe crear un pull request a la rama `develop` para su revisión y posterior fusión.

#### Commits

#### Analiis de codigo

```

```
... (1 línea restante)
Contraer
CONTRIBUTING.md
5 KB
# Licencia GNU Affero General Public License v3.0
LICENSE.md
1 KB