#######################
Django project template
#######################

This is a Django project template. It uses several best practices from
all around the place and is optimized for use under Python 3. There
shouldn't be any problems with it under older Pythons, though.
The idea is that the project should be fully configurable with environment variables.

Additionally, I prefer putting project specific apps inside an 'apps' module, which
gives us a way to have a nicer project structure in general.

To use this template, call `startproject` like this::

    django-admin.py startproject --template=https://github.com/julianwachholz/django-project-template/archive/master.zip -e=py,rst,html,gitignore {{ project_name }}

Also you can or should probably remove this section from the README file after starting a project with this command.

##################
{{ project_name }}
##################

This is the README file for {{ project_name }}.

Quickstart
==========

You'll be able to start working on this project with the following prerequisites:

- Python 2.7+ or 3.3+
- Django 1.7+
- ``pip`` and ``virtualenv``

You can roughly follow these simple commands to get a running application::

    $ virtualenv -p`which python3.3` {{ project_name }}-env
    $ source {{ project_name }}-env/bin/activate
    
    # Only required if you haven't setup your project yet. Remove these lines otherwise.
    $ pip install https://www.djangoproject.com/download/1.7b1/tarball/
    $ django-admin.py startproject --template=https://github.com/julianwachholz/django-project-template/archive/master.zip -e=py,rst,html {{ project_name }}

    $ # Append basic environment variables to environment setup
    $ echo "export DEBUG=1" >> {{ project_name }}-env/bin/activate
    $ echo "export PYTHONPATH=$PWD/{{ project_name }}" >> {{ project_name }}-env/bin/activate
    $ echo "export DJANGO_SETTINGS_MODULE={{ project_name }}.settings" >> {{ project_name }}-env/bin/activate
    $ source {{ project_name }}-env/bin/activate

    $ cd {{ project_name }}/
    $ pip install -r requirements.txt
    $ django-admin.py {migrate,runserver}

Of course, you'd want to setup a proper development environment.
Refer to the complete :doc:`docs/install` in this case.
