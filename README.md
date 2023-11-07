# With Travel in Mind

## Technologies Used

### Languages
- Python

### Frameworks, Libraries and Programs

- [Django REST Framework](https://www.django-rest-framework.org/)
  - High-level Python web framework used for building web API's.

- [Dj-Rest-Auth](https://pypi.org/project/dj-rest-auth/)
  - Drop-in API endpoints for handling authentication securely in Django REST Framework. 

- [Django-Filter](https://pypi.org/project/django-filter/) 
  - Library that allows to add filters based on specific conditions.

- [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
  - A JSON Web Token authentication plugin for the Django REST Framework.

- [PyJWT](https://pyjwt.readthedocs.io/en/stable/)
  - Python library which allows to encode and decode JSON Web Tokens (JWT).

- [Cloudinary](https://cloudinary.com/)
  - The cloud platform used to store the images.

- [Django Cloudinary Storage](https://pypi.org/project/django-cloudinary-storage/)
  - Django package that facilitates integration with Cloudinary by implementing Django Storage API. 

- [django-cors-headers](https://pypi.org/project/django-cors-headers/)
  - Allows in-browser requests to the Django application from other origins.

- [OAuthLib](https://pypi.org/project/oauthlib/)
  - Framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.

- [Requests-OAuthlib](https://requests-oauthlib.readthedocs.io/en/latest/)
  - uses the Python Requests and OAuthlib libraries to provide an easy-to-use Python interface for building OAuth1 and OAuth2 clients.

- [Pillow](https://pypi.org/project/Pillow/)
  - The Python Imaging Library that adds image processing capabilities to the Python interpreter.

- [psycopg2](https://pypi.org/project/psycopg2/)
  - PostgreSQL database adapter for the Python programming language.

- [Gunicorn](https://pypi.org/project/gunicorn/)
  - Python HTTP server for WSGI applications.

- [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/)
  - Django utility that allows to utilize the 12factor inspired DATABASE_URL environment variable to configure the Django application.

- [ElephantSQL](https://www.elephantsql.com/)
  - The database used by the deployed project on Heroku.

- [Git](https://git-scm.com/)
  - Version control system used in this project.

- [GitPod](https://www.gitpod.io/)
  - The IDE used to create the API.

- [GitHub](https://github.com/)
  - The code hosting platform used to save and store the files for this repository.

- [Heroku](https://www.heroku.com/)
  - The cloud platform used to deploy the project into live environment.

- [ASGI](https://asgi.readthedocs.io/en/latest/)
  - Asynchronous Server Gateway Interface (spiritual successor to WSGI) that is intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.

- [python3-openid](https://pypi.org/project/python3-openid/) 
  - A set of Python packages to support use of the OpenID decentralized identity system in the application, update to Python 3.

- [pytz](https://pypi.org/project/pytz/)
  - Library that allows time-zone calculations in Python applications and also allows us to create timezone aware datetime instances. 

- [sqlparse](https://pypi.org/project/sqlparse/)
  - A non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.


## Deployment

### Create a new external database

- Navigate to **ElephantSQL.com** and click **“Get a managed database today”**.

- Click **Create New Instance**.

- Set up your plan:
  - give your plan a Name;
  - select the Tiny Turtle (Free) plan.
  - the tags field can be left blank.

- Click **“Select Region”** and select a data center near you.

- Click **"Review"**, check that your details are correct and click **“Create instance”**.

- Return to the dashboard and click on the database instance name for this project.

- Copy the database URL.The URL starts with **postgres://**

### Create Heroku App

 - Sign up for Heroku and accept terms of service.

 - Click the **"Create a new app"** button.

 - Give your app a name and select the region closest to you. _A name must be **unique**._

### Install libraries

- Install **Gunicorn**(the server that is used to run Django on Heroku): `pip3 install gunicorn django-cors-headers`

- Install **dj_database_url** and **pyscopg2**(connect to PostegreSQL): `pip3 install dj_database_url pyscopg2`

- Install **Cloudinary** (The cloud platform used to store media files): `pip3 install dj3-cloudinary-storage`

### Get images stored on Cloudinary

- Create a Cloudinary account (steps can be found in the [Code Institutes](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/9236975633b64a12a61a00e0cca7c47d/?child=first) tutorial in LMS).

- **settings.py**:

  - Add Cloudinary Libraries to installed apps (the order is important):

    ````
    INSTALLED_APPS = [
      ...,
      'cloudinary_storage',
      'django.contrib.staticfiles',
      'cloudinary',
      ...,
    ]
    ````
  
  - Add following just below imports and `if os.path.exists`:
   
    ````
    CLOUDINARY_STORAGE = {
        'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
    }

    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ````

### Create an env.py file

- Create **env.py** file and check that the file is included in the **.gitignore file**.

- Import os library: `import os`.

- Set environment variables:
  - **DATABASE_URL** with the value you just copied from ElephantSQL: `os.environ["DATABASE_URL"]="<copiedURL>`
  - **SECRET_KEY**: `os.environ["SECRET_KEY"] = "randomSecretKey"` ([Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) was used to generate a secret key).
  - **DEV**: `'1'`.
  - **CLOUDINARY_URL** with the value copied from the dashboard (remove `CLOUDINARY_URL` in the beginning).