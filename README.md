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

## Deploy

* virtualenv (para aislar los paquetes de producción https://virtualenv.pypa.io/en/latest/)
* gunicorn (servidor WSGI HTTP http://gunicorn.org/)
* supervisor (supervisor de procesos http://supervisord.org/)
* nginx (HTTP server http://nginx.org/)
* postgresql (DB http://www.postgresql.org/)

Cabe hacer notar que este deploy estas basado en Digital Ocean con una
imagen de Debian 8 (jessie) sin embargo debiese aplicar para la mayoria 
de los sistemas operativos GNU/Linux

En primer lugar debemos instalar ciertas herramientas

    sudo apt-get update
    sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib nginx
    
### Postgresql

    sudo su - postgres
    psql
    CREATE DATABASE myproject;
    CREATE USER myprojectuser WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
    \q
    exit
    
### Virtualenv

    sudo pip install virtualenv
    mkdir ~/myproject
    cd ~/myproject
    virtualenv myprojectenv
    source myprojectenv/bin/activate
    pip install django gunicorn psycopg2


### Gunicorn 

```bash

```

### Supervisor


### Nginx

    sudo nano /etc/nginx/sites-available/myproject

## Git Commit Guidelines

### Type
Must be one of the following:

* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Documentation only changes
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing
  semi-colons, etc)
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **perf**: A code change that improves performance
* **test**: Adding missing tests
* **chore**: Changes to the build process or auxiliary tools and libraries such as documentation
  generation

