FROM python:3.9

WORKDIR /app

COPY /app /app

RUN apt-get update && apt-get install -y libgl1-mesa-glx

RUN pip install -r requirements.txt

RUN pip uninstall -y Pillow

RUN pip install Pillow==9.0.1

CMD ["python3.9", "main.py"]

