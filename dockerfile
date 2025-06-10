FROM python:3.12-slim

WORKDIR /app

COPY requerimentos.txt .
RUN pip install --no-cache-dir -r requerimentos.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]