# Wagtail-blog - dockerized demo of the Wagtail blog app

## Installing

        git clone https://github.com/pasiol/wagtail-blog.git
        
Install Python virtual environment to the project folder and activate it.

        python3 -m venv .venv
        source .venv/bin/activate
        python manage.py migrate

## Running locally dev environment

On the Python virtual environment:

        python manage.py runserver 0:8000

### Building docker container

        docker build -t wagtail_blog .

### Running local docker dev environment

         docker run --rm -p 8000:8000 -v $PWD/sqlite:/app/sqlite -e SITE_NAME="Blog-app demo" wagtail_blog

![Welcome page after the installation](images/server.PNG)