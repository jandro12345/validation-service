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