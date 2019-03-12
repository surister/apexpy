=======================
Installation and Set up
=======================

.. _install:

Downloading the library:
------------------------

Using bare git::

    $ git clone https://github.com/surister/apexpy.git

Using pip::

    $ pip install apexlegendspy

Using pipenv::

    $ pipenv install apexlegendspy

Get an Api key
--------------
To get your api key go `here <https://apex.tracker.gg/site-api>`_ and follow the steps.

Providing your Api Key
----------------------
Any api key should remain secret for your only use, to avoid leaking your key, you have it as an
environment variable **APEX_LEY=actual_key** apexpy will look for it automatically.

.. note::
    Quick way to have this done:

    1. Install dotenv::

        $ pip install python-dotenv
                                        or
        $ pipenv install python-dotenv

    2. Create a .env file and put there your api key as::

        APEX_KEY=KEY


    *Apexpy automatically loads dotenv files if python-dotenv is installed*


