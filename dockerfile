FROM python:3.9-slim

WORKDIR /app

COPY ./app.py .
COPY ./app_teste.py .
COPY ./requerements.txt .
  
RUN pip install -r requerements.txt

EXPOSE 5000

CMD ["python","app.py"]
