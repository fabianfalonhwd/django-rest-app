# Django rest framework

Test django rest framework

## Development Environment

At the bare minimum you'll need the following for your development environment:

1. [Python](http://www.python.org/)
2. [MySQL](http://www.mysql.com/)

It is strongly recommended to also install and use the following tools:

1. [virtualenv](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenv)
2. [virtualenvwrapper](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenvwrapper)

### Local Setup

The following assumes you have all of the recommended tools listed above installed.

#### 1. Clone the project:

    $ git clone https://github.com/fabianfalonhwd/django-rest-app.git
    $ cd website

#### 2. Create and initialize virtualenv for the project:

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

#### 3. Upgrade the database:

    $ python manage.py makemigrations
    $ python manage.py migrate

#### 4. Run the development server:

    $ python manage.py runserver


#### 5. Open [http://localhost:5000](http://localhost:8000)

