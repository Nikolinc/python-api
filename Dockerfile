FROM python:3.10

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Запуск приложения
CMD ["python", "main.py"]
