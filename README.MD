Build docker db image

`docker run -d --name facilito -p 5436:5432 -e POSTGRES_PASSWORD=facilito -e POSTGRES_DB=facilito -e POSTGRES_USER=facilito postgres`


# poetry commands
para añadir librerias al proyecto al entorno virtual
$ poetry add psycopg2-binary

para correr el proyecto

$ poetry run python manage.py runserver

para migrar en la abse de datos

$ poetry run python manage.py migrate



para hacer copia de seguridad de la base de datos

$ poetry run python manage.py dumpdata products.product --format=json --indent=4 > products/fixtures/products.json

la ruta despues de > es donde se guarda el archivo json con el respaldo de la base de datos

Para restaurar esa copia de seguridad

$ poetry run python manage.py loaddata products.json


--settings=smartbouncer.settings.prd


