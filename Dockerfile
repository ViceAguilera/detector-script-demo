FROM python:3.9

WORKDIR /app

COPY /app /app

RUN pip install -r requirements.txt

RUN pip uninstall -y Pillow

RUN pip install Pillow==9.0.1

CMD ["python3.9", "main.py"]

