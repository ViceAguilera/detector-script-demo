
#Se instalan las librerias.
RUN pip install -r requirements.txt
#Se elimina una libreria que no es compatible con el proyecto.
RUN pip uninstall -y Pillow
#se instala la version 9.0.1 de la libreria Pillow.
RUN pip install Pillow==9.0.1
#Se ejecuta el script.
RUN python3.9 main.py

