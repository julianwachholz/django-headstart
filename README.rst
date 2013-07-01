#######################
Django project template
#######################

This is a django project template. It uses several best practices and is my own
version of the twoscoops project template. A major difference though is the use
of a single settings file (except for test settings). The idea is that the
project should be fully configurable with environment variables.

To use this template, call `startproject` like this::

    django-admin.py startproject --template=/path/to/folder -e=py,rst,html,gitignore {{ project_name }}

Also you can or should probably remove this section from the readme after doing so.

#########################
{{ project_name }} readme
#########################

This is the README file for {{ project_name }}.

Quickstart
==========

You'll be able to start working on this project with the following prerequisites:

- Python 2.7
- ``pip``
- ``virtualenv``, ``virtualenvwrapper``

Use the following commands to get a running application::

    $ mkvirtualenv -p python27 {{ project_name }}
    $ cd {{ project_name }} && add2virtualenv `pwd`
    $ workon {{ project_name }}
    $ pip install -r requirements/local.txt
    $ export DJANGO_SETTINGS_MODULE='{{ project_name }}.settings.base'
    $ django-admin.py {syncdb,migrate,runserver}

Of course, you'd want to setup a proper development environment.
Refer to the complete :doc:`docs/install` in this case.
