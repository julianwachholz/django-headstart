############
Installation
############

This document serves as a guide to get your local development environment for `{{ project_name }}` up and running.


*************
Prerequisites
*************

Make sure you have a working installation of the following packages:

- git
- Python 2.7
- pip
- virtualenv
- PostgreSQL

Once you've installed these, clone the repository and move on to the next step::

    git clone $REPOSITORY_URL

Virtualenv
==========

Create a virtualenv for this project with a Python 2.7 binary. It is recommended that you
use ``virtualenvwrapper`` for a clean project directory::

    $ mkvirtualenv -p python27 {{ project_name }}
    $ cd {{ project_name }} && add2virtualenv `pwd`
    $ workon {{ project_name }}

Requirements
============

Activate your virtual environment once you installed it using ``workon {{ project_name }}``.
After this, you'll want to install the project requirements::

    $ pip install -r requirements/local.txt

This will install all dependencies listed in requirements/_base.txt and requirements/local.txt. These include all
project libraries as well as testing and documentation tools.

*************
Configuration
*************

Confidential settings such as ``SECRET_KEY`` and database passwords are not stored in the project's main settings
files, but are saved in environment dependent variables.

.. envvar:: DJANGO_SETTINGS_MODULE

    If you do not want to specify the settings module to use every time you use a command, you can set
    the according environment variable for this, here we set it to the local settings::

        $ export DJANGO_SETTINGS_MODULE='{{ project_url }}.settings.local


.. envvar:: SECRET_KEY

    This sets the ``SECRET_KEY`` for Django, usually a random String from ``django-admin.py startproject``.
    Since every installation is independent, you'll have to generate one for yourself.

.. envvar:: DATABASE_URL

    Used to create the ``DATABASES`` dict for Django.
    Currently only the 'default' database is set. See `dj-database-url`_ for examples.

.. envvar:: MANDRILL_API_KEY

    `Mandrill`_ API key for email sending by MailChimp/Mandrill.

.. todo:: Make sure to list every environment variable here.

.. _dj-database-url: https://github.com/kennethreitz/dj-database-url
.. _Mandrill: http://mandrill.com/

Using virtualenvwrapper
=======================

``virtualenvwrapper`` comes with predefined hooks that are run on certain events. Using these we'll be able
to define environment variables needed to run the project with ease.

You can define these environment variables in the **postactivate** hook in your **$VIRTUAL_ENV/bin** directory:

.. code-block:: sh

    #!/bin/sh
    # This hook is run after this virtualenv is activated.

    export DJANGO_SETTINGS_MODULE='{{ project_name }}.settings.base'
    export SECRET_KEY='secr3t'
    export DATABASE_URL='postgres://user:pass@localhost/{{ project_name }}'

Make sure you ``unset`` the variables set in **postactivate** again in **postdeactivate**

Using PyCharm
=============

`PyCharm`_ is a Java-based IDE for Python and Django development. It integrates many tools
that we are using in this project. Setting up the above environment variables is done via the run configuration
for the specific task.

1. From the menu, select :menuselection:`R&un --> Edit Configu&rations`
2. Setup your run configuration as seen in the screenshot below.

.. image:: images/pycharm_run_config.png
    :scale: 100%

3. You can configure the environment variables in the according dialog:

.. image:: images/pycharm_run_config_env.png
    :scale: 100%

.. _PyCharm: http://www.jetbrains.com/pycharm/

***********************
Running the test server
***********************

Once you're set up with all of the above, running the local development server of Django is just a few commands
away::

    $ django-admin.py {syncdb,migrate}
    $ django-admin.py createsuperuser
    $ django-admin.py runserver

Once you're done with these steps you might be interested in :doc:`running it in production <deploy>`

Where's ``manage.py``?
======================

To prevent any mistakes made by relying on relative imports, this project comes without a **manage.py** file.
Django gives us the tools and configuration needed to run everything without it.
To start, you'll have to include the project root in your :envvar:`PYTHONPATH`. We already did this by using
the `add2virtualenv` command. After setting up the correct path and environment, you'll be able to just call
``django-admin.py`` (Suggestion: create a simple alias for it in your shell to save typing).
