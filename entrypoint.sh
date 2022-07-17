
#!/bin/bash


if [ "$POSTGRES_DB" = "wedding_db" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py makemigrations
python manage.py migrate
exec "$@"

