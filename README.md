django-userena-dev
==================

Install requirements
--------------------

**Django duke client**

```bash
$ git clone https://github.com/h3/django-duke-client.git
$ cd django-duke-client/
$ sudo python setup.py develop
```

Setup dev environment
---------------------

```bash
$ git clone https://github.com/h3/django-userena-dev.git
$ cd django-userena-dev/
$ duke init userena_dev/
$ buildout
$ cd userena_dev/
$ syncdb
$ migrate guardian
$ migrate userena
$ runserver
```
