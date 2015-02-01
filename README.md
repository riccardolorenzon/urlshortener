Django URLShortener
================

A Django application that adds an URL shortener to your site similar to bit.ly picking the shorter url path from a pre filled list of values.

Installation
------------

If you are inside a virtual environment, activate it before installing Django:
    source <your env dir>/bin/activate

You need to install the following prerequisites in order to use this app:

    pip install django
    pip install python-dateutil

Clone the repository from github or unzip if you previously downloaded(from github or any other source)
    git clone --bare https://github.com/riccardolorenzon/urlshortener.git

Run development server using the following command(in the directory ./urlshortener):
    python manage.py runserver 8000

Open in your browser the dev server url:
    http://127.0.0.1:8000/

If you want to clone it from github