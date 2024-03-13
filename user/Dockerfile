FROM python:3.9-slim

COPY app.py /app/

WORKDIR /app

RUN pip install --no-cache-dir flask

CMD ["python", "app.py"]