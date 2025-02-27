# validation-service
```
gunicorn app:app --log-level DEBUG --reload --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:9001 -c gunicorn_config.py
```

# Postgresql

```
docker run --name pg \
    -e POSTGRES_PASSWORD=Pg.2025.appYk23_pg \
    -e POSTGRES_USER=app_pg \
    -e POSTGRES_DB=app_pg \
    -e PGDATA=/var/lib/postgresql/data \
    -v ./pg_app/data:/var/lib/postgresql/data \
    -p 5432:5432 \
    -d postgres
```

# RabbitMQ
```
docker run -d --name rabbit-queue -p 5672:5672 -p 15672:15672 rabbitmq:management
```


# Guide
```
Ejecutar el docker con el servicio de Postgresql

docker run --name pg \
    -e POSTGRES_PASSWORD=Pg.2025.appYk23_pg \
    -e POSTGRES_USER=app_pg \
    -e POSTGRES_DB=app_pg \
    -e PGDATA=/var/lib/postgresql/data \
    -v ./pg_app/data:/var/lib/postgresql/data \
    -p 5432:5432 \
    -d postgres

Ejecutar el servicio validation-service

gunicorn app:app --log-level DEBUG --reload --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:9001 -c gunicorn_config.py

Ejecutar el RabbitMQ

docker run -d --name rabbit-queue -p 5672:5672 -p 15672:15672 rabbitmq:management

Ejecutar el servicio service-consumer

gunicorn consumer:app --log-level DEBUG --reload --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:9002

La Api estara a la escucha en el puerto :9001
```