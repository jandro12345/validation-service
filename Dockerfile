FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9001

CMD ["gunicorn", "app:app", "--log-level", "DEBUG", "--reload", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:9001", "-c", "gunicorn_config.py"]