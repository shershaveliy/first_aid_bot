FROM python:3.10-slim

# Создаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ВСЕ файлы проекта (включая папку src)
COPY . .

# Указываем правильный путь к main.py
CMD ["python", "src/main.py"]