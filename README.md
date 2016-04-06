# condominios

## Docker

En caso de usar docker el proyecto provee un docker file para web y un
docker compose para el proyecto completo (el cual usa una imagen de docker postgresql)

* docker-compose build (solo para construir cuando se cambia estructura)
* docker-compose up

* docker-compose run name_instance command params (esto ejecuta el comando -command- en el docker de nombre name_instance)

## Dependencias

El archivo requirements.txt contiene las dependencias del proyecto 

## DB - migrate

Al ejecutar un migrate no olvidar que nuestra apps deben ser añadidas a mano

* python manage.py makemigrations app_name
* python manage.py migrate

Con esto nos aseguramos de tener todas las relaciones dentro del módulo de migrate. 

## Django Rest Framework

Para construir modelos de REST aplicamos 

* serializer.py (esto crea un serializador en base al modelo)
* view.py (aqui definimos el viewSet)
* urls.py -condominios/urls.py- (se importa para el router)