![Python Canarias Logo](https://github.com/pythoncanarias/docs/raw/master/logos/python-canarias/bitmaps/logo-python-canarias-color-372x128.png)

Welcome to the Website of [Python Canarias](pythoncanarias.es) 🚀 happily made with [Django](https://www.djangoproject.com/).

---

## Table of contents : <!-- omit in TOC -->

- [Python dependencies](#python-dependencies)
- [Node.js dependencies](#nodejs-dependencies)
- [EditorConfig](#editorconfig)
- [Customize your settings](#customize-your-settings)
- [Database](#database)
- [Media](#media)
- [Launching services](#launching-services)
- [API](#api)
- [Adding a new section (app) to the project](#adding-a-new-section-app-to-the-project)

## Python dependencies

This project recommends the use of virtual environments. The [`requirements.txt`](requirements.txt) contains the packages for _production_, while [`requirements-dev.txt`](requirements-dev.txt) includes the additional requirements for _development_.

Some advantages of using **virtual environment** are:

- Isolates the Python environment from the system.
- It is easy to duplicate the production environment.
- It is easy to duplicate the development environment.
- GitHub enables security checks on the requirements files.
- You can use [`virtualenv-wrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/), which is ❤️.

🐍 **Note**: The procedure assumes `python3` in your system executes a version of
**Python 3.6** or upper.

1. Install [`virtualenv`](https://virtualenv.pypa.io/en/latest/) and (encouragingly) [`virtualenv-wrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/).
2. Clone the repository: `git clone git@github.com:pythoncanarias/web.git`
3. Change to the project directory. Create the virtual environment and install all
   the dependencies for the project with the next lines:

```console
    $ mkvirtualenv -a . -p $(which python3) pycanweb
    $ pip install requirements.txt
    $ pip install requirements-dev.txt  # For developers
```

> This will install a virtual environment called `pycanweb` for the project, with Python 3, Django and all the rest Python dependencies.

## Node.js dependencies

Minimal versions of the required tools:

- `npm >= 5.6.0`
- `node >= 9.11.2`
- `gulp (cli) >= 2.0.1`
- `gulp (local version) >= 4.0.0`

There are some libraries (_css, js_) used on either the _frontend_ or the _development phase_. To install them, make:

```console
$ npm install
```

> ⚠️ This will create a bunch of folders and files under `node_modules`.

In order to use `gulp` correctly it is necessary to install:

```console
$ sudo npm install --global gulp-cli
```

## EditorConfig

Please install the corresponding extension of [EditorConfig](https://editorconfig.org/) in your favorite editor. Thus your editor will pick the settings stored in `.editorconfig`.

This configuration avoids conflicts with a lot of settings, mainly with tabs widths.

## Customize your settings

Feel free to change some of the settings creating a file called `.env` on the root of the project.

## Database

We are using **PostgreSQL** as _database management system_. In order to configure the project correctly it is important to follow some indications:

1. Install [PostgreSQL](https://www.postgresql.org/download/).
2. Create a _database_ and a _user/password_ with full access to that database.
3. Set the following keys in the `.env` file: `DATABASE_NAME`, `DATABASE_USER` and `DATABASE_PASSWORD`.

Afterwards you can apply migrations with:

```console
$ workon pycanweb  # Activation of virtualenv
$ ./manage.py migrate
```

### Admin user <!-- omit in TOC -->

In order to create a user for the admin site of Django you should:

```console
$ workon pycanweb
$ ./manage.py createsuperuser
```

### Fixtures <!-- omit in TOC -->

Initially (and obviously) the database will be empty. Some `fixtures` will be needed to work with.

## Media

It is important to properly set the key `MEDIA_ROOT` in the file `.env` for the server to locate the media assets.

## Launching services

In order to properly develop, you have to launch the following services:

- _Django_ development server:

```console
    $ workon pycanweb
    $ ./manage.py runserver
```

- _Gulp_ build system for static assets:

```console
    $ gulp watch
```

After that, you'll be able to access the project on: http://127.0.0.1:8000

> The changes made both in Python files or static files will be detected by the services and will reload them.

## API

You can check the documentation of the [public API](./docs/api.md).

## Adding a new section (app) to the project

Normally, when a new app (section) is needed in a Django project, it can be created as follows:

```console
$ ./manage.py startapp <app>
```

Based on the design of our project, some further steps must be taken in order to get the app well visualized:

1. Add `<app>` to the `APPS` constant on [gulp/config.js](gulp/config.js).
2. Create the file `<app>/static/<app>/css/main.scss` with, at least, the following content: `@import "commons/static/commons/css/base";`
3. Create the base template file at `<app>/templates/<app>/base.html` which extends from [commons/templates/base.html](commons/templates/base.html) as `base.html` and links to the stylesheet `<app>/custom.min.css` (_this file is generated by gulp_)
4. In order to create the corresponding item on header menu, add the app entry at [commons/templates/header.html](commons/templates/header.html).
