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

## Database Diagram

The database model diagram was designed using [Lucidchart](https://www.lucidchart.com/pages/sv).

The initial plan was developed during the project. There have been some changes made to a few fields and a new model, CommentLike, has been implemented.

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1700780451/Database_Diagram_futqfk.png)

<details><summary>Click here to see the origin database diagram</summary>

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1699365141/database_diagram_i4npl4.png)
</details>

### Explorer Model

- The model has a one-to-one relationship with the Django User model. This means that for every User that signs up to the website, there will be a corresponding Explorer model which is used to define some additional values relative to the user. 

- Is based on the "Django REST Framework" walkthrough project. 

- Some adjustments and additions were made to fit the needs of my project:
  - The `content` field has been renamed to `bio`.
  - New fields added:
    - `region_you_would_like_to_explore` (an explorer can choose among 7 region, the field is _optional_)
    - `dream_destination`(the field is _optional_).

### Post Model

- The model represents the posts made by users. 

- Keeps track of the times when each post was created and last updated.

- Is based on the "Django REST Framework" walkthrough project. 

- Some adjustments and additions were made to fit the needs of my project:
  - The `content` field has been renamed to `description`.
  - New fields added:
    - `place` (Explorers can specify the country represented in the image for this travel project).
    - `region` (Explorers can choose among 7 regions).

### Comment Model

- Enables the user to create a comment.

- Keeps track of the times when each comment was created and last updated.

- Is based on the "Django REST Framework" walkthrough project. 

- The `content` field has been renamed to `comment`.

### Like Model

- The model represents the likes given by users to a post.

- **'unique_together'** makes sure a user can't like the same post twice.

- Is based on the "Django REST Framework" walkthrough project.

### Follower Model 

- The model related to 'owner' and 'followed'.
    - 'owner' is a User that is following a User.
    - 'followed' is a User that is followed by 'owner'.
  
- **'unique_together'** makes sure a user can't 'double follow' the same user.

- Is based on the "Django REST Framework" walkthrough project.

### Bookmark Model

- The custom model.

- The model represents the list of posts that a user wants to keep track of. 

- **'unique_together'** makes sure a user can't 'double bookmark' the same post. 

### Favourite Model 

- The custom model.

- The model enables user to add other users to "favourites".

- The model related to 'owner' and 'favorited'.
    - 'owner' is a User that is favoriting a User.
    - 'favorited' is a User that is favorited by 'owner'.

- **'unique_together'** makes sure a user can't 'double favorite' the same user.

### CommentLike Model

- The custom model.

- The model represents the likes given by users to a comment.

- **'unique_together'** makes sure a user can't like the same comment twice.

## API Endpoints

### Posts

#### /posts

| Feature | Status |
|---------------|--------|
| Correct URL path | :white_check_mark: |
|	Add post functionality available for ONLY logged-in user  | :white_check_mark: |
| Validation works correctly | :white_check_mark: |
|	Correct post fields | :white_check_mark: |
|	Search functionality | :white_check_mark: |
|	Filter functionality | :white_check_mark: |
|	Ordering functionality | :white_check_mark: |
|	Correct URL for the default image | :white_check_mark: |
|	Pagination functionality | :white_check_mark: |
|	Likes_count field working correctly | :white_check_mark: |
|	Comments_count field working correctly | :white_check_mark: |
|	Bookmarks_count field working correctly | :white_check_mark: |

#### /posts/id

| Feature | Status |
|---------------|--------|
| Correct URL path | :white_check_mark: |
| Returns detail about the selected post | :white_check_mark: |
|	Only authenticated owners can update their own posts | :white_check_mark: |
|	Only authenticated owners can delete their own posts | :white_check_mark: |

## Testing

### Validator Testing

**Validator**: [CI Python Linter](https://pep8ci.herokuapp.com/)

Only files with custom-written Python code have been verified with the validator. 

<details>
<summary>with_travel_in_mind_api</summary>
  
- permissions.py
- serializers.py
- settings.py
- views.py
- urls.py
</details>

<details>
<summary>explorers</summary>
  
- models.py
- serializers.py
- views.py
- urls.py
- admin.py
- tests.py
</details>

<details>
<summary>posts</summary>
  
- models.py
- serializers.py
- views.py
- urls.py
- tests.py
- admin.py
</details>

<details>
<summary>comments</summary>
  
- models.py
- serializers.py
- views.py
- urls.py
- admin.py
</details>

<details>
<summary>likes</summary>
  
- models.py
- serializers.py
- views.py
- urls.py
- admin.py
</details>

<details>
<summary>followers</summary>
  
- models.py
- serializers.py
- views.py
- urls.py
- admin.py
</details>

<details>
<summary>bookmarks</summary>
  
- models.py
- serializers.py
- views.py
- urls.py
- admin.py
</details>

<details>
<summary>favourites</summary>
  
- models.py
- serializers.py
- views.py
- urls.py
- admin.py
</details>

<details>
<summary>commentlikes</summary>
  
- models.py
- serializers.py
- views.py
- urls.py
- admin.py
</details>

Minor indentation, trailing whitespace and no new line/blank line at end of file errors were corrected. No known errors are now present. All the files tested got the result below.

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697580394/static/images/ci_python_linter.286469fc4bb0.png)

### Automated testing

Automated tests were created and run on the With Travel In Mind API to test basic CRUD functionality and user permissions for the Post and Explorer models. 

Result: 

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1699391307/automated_testing_tpvfli.png)

<details>
<summary>PostListViewTests</summary>

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1699392677/post_list_test_views_es2bnf.png)

</details>

<details>
<summary>PostDetailViewTests</summary>

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1699392919/post_detail_view_tests_1_rm3wsc.png)
![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1699392919/post_detail_view_tests_2_tpti8d.png)

</details>

<details>
<summary>ExplorerListViewTests</summary>

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1699393277/explorer_list_view_tests_idxh6x.png)

</details>

<details>
<summary>ExplorerDetailViewTests</summary>

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1699393277/explorer_detail_view_tests_y5uehc.png)

</details>

## Credits

### Content

- The main code of this project is based on the tutorial "Django REST Framework" by Code Institute. The project was expanded with custom models and functionality to suit my needs. To better understand the subject and challenge myself, I chose to write views for Explorer and Post, which were later refactored to generic views.

- Inspiration to my two custom models ("Bookmark" and "Favourite") was taken from [Instagram](https://www.instagram.com/).

- [Django REST Framework Documentation](https://www.django-rest-framework.org/) was used throughout the project to gain more knowledge about different concepts.

- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) was used to generate Django Secret Key.

## Deployment

### Create Heroku App

 - Sign up for Heroku and accept terms of service.

 - Click the **"Create a new app"** button.

 - Give your app a name and select the region closest to you. _A name must be **unique**._

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

#### Connect to external database:

- Install **dj_database_url** and **pyscopg2**(connect to PostgreSQL): `pip3 install dj_database_url pyscopg2`

- Add the following import in **settings.py**:

  ````
  import dj_database_url
  ````
- Separate the development and production databases by replacing the **DATABASES** variable with the following code:

  ````
  if 'DEV' in os.environ:
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.sqlite3',
              'NAME': BASE_DIR / 'db.sqlite3',
          }
      }
  else:
      DATABASES = {
          'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
      }
  ````

- Add the following environment variable in **env.py**:
  - **DATABASE_URL** with the value you copied from ElephantSQL: `os.environ["DATABASE_URL"]="<copiedURL>`

- Add a print statement to the DATABASES section above to confirm you have connected to the external database (Run `python3 manage.py makemigrations --dry-run`). Delete the print statement.

- Save all files and make migrations: `python3 manage.py migrate`

- Create a superuser for your new database: `python3 manage.py createsuperuser`

- Confirm that the data in your database on ElephantSQL has been created: 
  - On the ElephantSQL page for your database, in the left side navigation, select **“BROWSER”**.
  - Click the **Table queries** button, select **auth_user**.
  - When you click **“Execute”**, you should see your newly created superuser details displayed. This confirms your tables have been created and you can add data to your database.

### Install more libraries

- Install **Gunicorn**(the server that is used to run Django on Heroku): `pip3 install gunicorn django-cors-headers`

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
  - **SECRET_KEY**: `os.environ["SECRET_KEY"] = "randomSecretKey"` ([Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) was used to generate a secret key).
  - **DEV**: `'1'`.
  - **CLOUDINARY_URL** with the value copied from the dashboard (remove `CLOUDINARY_URL` in the beginning).

### Update settings.py

- Remove the insecure secret key provided by Django. Change your SECRET_KEY variable to the following: `SECRET_KEY = os.environ.get('SECRET_KEY')`

- Add **corsheaders** into **INSTALLED_APPS**:
  
  ````
  INSTALLED_APPS = [
    ...
    'dj_rest_auth.registration',
    'corsheaders',
    ...
  ]
  ````

- Add **corsheaders middleware** to the TOP of the MIDDLEWARE.

- Add the following code to allow network requests made to the server: 

  ````
  if 'CLIENT_ORIGIN' in os.environ:
      CORS_ALLOWED_ORIGINS = [
          os.environ.get('CLIENT_ORIGIN')
      ]
  else:
      CORS_ALLOWED_ORIGIN_REGEXES = [
          r"^https://.*\.gitpod\.io$",
      ]
  ````

- Add the following code to allow cookies: `CORS_ALLOW_CREDENTIALS = True`

- To be able to have the front end app and the API deployed to different platforms, set the **JWT_AUTH_SAMESITE** attribute to **'None'**. 

- Set the DEBUG value to be **True only if the DEV environment variable exists**:

  `DEBUG = 'DEV' in os.environ`

- Add Heroku Hostname to ALLOWED_HOSTS

  ````
  ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
  ````

### Ensure the project requirements.txt file is up to date.
  
  ````
  pip freeze --local > requirements.txt
  ````

### Create a Procfile

  ````
  release: python manage.py makemigrations && python manage.py migrate
  web: gunicorn with_travel_in_mind_api.wsgi
  ````

### Go back to Heroku

- Go to the Heroku dashboard and open the **Settings** tab:

- Ensure that following _Config Vars_ are added:
  - KEY: **SECRET_KEY** | VALUE: **randomSecretKey**(the value that is in env.py)
  - KEY: **DATABASE_URL** | VALUE: **ElephantSQL database url**(no quotation marks needed)
  - KEY: **DISABLE_COLLECTSTATIC** | VALUE: **1** (Temporary to be able to deploy the project as we do not have any static files yet)
  - KEY **CLOUDINARY_URL** | VALUE: **API Environment Variable** copied in the Cloudinary dashboard.

- Click on the **"Deploy"** section on the top of the page.

- Select **GitHub** as deployment method and click the **"Connect to GitHub"** button.

- Search for the repository for this project, _with_travel_in_mind_api_. 

- Click **"Connect"** to link up Heroku app to the GitHub repository.

- Click on **"Deploy Branch"**.

- **Optional**: Click the **"Enable Automatic Deploys"** button to make it possible for Heroku to rebuild the app a new change is pushed to GitHub repository.

### Make some changes in order to use this API with the upcoming Front End project.

- **Adding ALLOWED_HOSTS**:

  - Add the following to the _Config_Vars_ on **Heroku**:

    `KEY **ALLOWED_HOST** | VALUE: **'app-name.herokuapp.com'**`

  - Update ALLOWED_HOSTS to in the **settings.py**:

    `ALLOWED_HOSTS = ['localhost', os.environ.get('ALLOWED_HOST')]`

- **Adding CLIENT_ORIGIN_DEV**:

  - Using GitPod:
   
    - `import re` in the top of settings.py

    - Replace the else statement and body for **if 'CLIENT_ORIGIN' in os.environ:** with the following code:

      ````
      if 'CLIENT_ORIGIN_DEV' in os.environ:
          extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
          CORS_ALLOWED_ORIGIN_REGEXES = [
              rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
          ]
      ````
  - Using Codeanywhere:
   
    - `import re` in the top of settings.py

    - Replace the else statement and body for **if 'CLIENT_ORIGIN' in os.environ:** with the following code:

      ````
      if 'CLIENT_ORIGIN_DEV' in os.environ:
          extracted_url = re.match(r'^([^.]+)', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)

          CORS_ALLOWED_ORIGIN_REGEXES = [
              rf"{extracted_url}.(eu|us)\d+\.codeanyapp\.com$",
          ]
      ````
- **Git add, commit and push** the changes to your settings.py file to GitHub.

- Go to Heroku. Click on the **"Deploy"** section on the top of the page. Click on **"Deploy Branch"**.

### Tell the API to accept request from the React project.

- Go to the Heroku dashboard and open the **Settings** tab:

- Add following _Config_Vars_:
  
  - KEY: `CLIENT_ORIGIN` | VALUE: `app-name.herokuapp.com` (The deployed React project)
  - KEY: `CLIENT_ORIGIN_DEV` | VALUE: `3000-kattis91-app-name.gitpod.io` (Gitpod Preview link)

## Development 

## Fork

- Log in to **GitHub** and find the repository for this project, [_Kattis91/with_travel_in_mind_api_](https://github.com/Kattis91/with-travel-in-mind-api).

- In the top-right corner of the page, click **Fork**.

- Type some new name into the "Repository name" field to distinguish your fork from the upstream repository.

- Click **Create Fork**.

- The fork is now in your personal account and can be changed in the way you want.

## Clone

- On **GitHub**, navigate to your fork of the _Kattis91/with_travel_in_mind_api_ repository.

- Above the list of files, click **<>Code**.

- Copy the **URL** for the repository. Repository can be cloned in three different ways:
  - **HTTPS**;
  - **SSH**;
  - **GitHub CLI**.

- Open Terminal and change the current working directory to the location where you want the cloned directory.

- Type `git clone`, and paste the URL you copied earlier. Press **Enter**