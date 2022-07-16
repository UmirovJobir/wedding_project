
#!/bin/bash


if [ "$POSTGRES_DB" = "wedding_project_db" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"

python3 manage.py makemigrations
python3 manage.py migrate