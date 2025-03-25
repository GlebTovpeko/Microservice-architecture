FROM python:3.9

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости первыми для кэширования
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY app/ .

EXPOSE 6080

# Явно указываем путь к Python и модуль запуска
CMD ["python", "-m", "gunicorn", "--bind", ":6080", "app:app"]