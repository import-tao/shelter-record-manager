# Shelter-Record-Manager
This is a project to build an app to manage the day to day running of an animal shelter.

## Git Crash Course to Start Contributing
At a high level, here’s how we suggest you go about proposing a change to this project:

1. [Fork this project](https://help.github.com/articles/fork-a-repo/) to your account.
2. [Create a branch](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository) for the change you intend to make.
3. Make your changes to your fork.
4. [Send a pull request](https://help.github.com/articles/using-pull-requests/) from your fork’s branch to our master branch.

Click on the hyperlinks for a more detailed walk through of how to do each step.

## How to get up and running

Before we get started the below assumes that you have python installed. This project has been created using 3.6. If you do not have python, see the [python website](https://www.python.org/downloads/) to download it.
If you have multiple versions of python installed on your computer, where it refers to typing "python" in the cmd line, you will need to specify which one you have e.g.

``` shell
python3
```

If you are using any version of Python older than 3.4 (and that includes the 2.7 release), virtual environments are not supported natively. For those versions of Python, you need to download and install a third-party tool called virtualenv before you can create virtual environments.

### Step 1 - Create Secret Key file

All of the settings are stored within a file named "secret_environment_keys.py" which is imported into "settings.py". You will see at the top of settings.py it imports Config.

Within the settings folder (shelter>settings) add in the following code to a file called "secret_environment_keys.py":

``` python
import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or '*CONTACT REPO CONTRIBUTOR FOR THIS*'

    # Email settings which are not required
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD") or '*EMAIL PASSWORD*'
    EMAIL_HOST = os.environ.get('EMAIL_HOST') or '*EMAIL HOST*'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') or '*EMAIL ADDRESS*'
    EMAIL_PORT = int(os.environ.get("EMAIL_PORT") or *EMAIL PORT*)
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL') or 'My Animal Shelter <*EMAIL ADDRESS*>'
    ADMINS =  (
        "Dev", "*EMAIL ADDRESS*"),
    )
```

Anything in stars needs to be added in. Note that only the SECRET_KEY is required to start Django and if you do not have this, Django will not run.

Your shelter folder should now look like this:

```
+---shelter
|       +--catalog
|       +--shelter
|           +--settings
|               |...
|               |secret_environment_keys.py
|       +--templates
|       .gitignote
|       manage.py

+---README.md
+---requirments.txt
+---UI-notes.txt
```

### Step 2 - Create virtual Environment

This will use venv package built into [python](https://docs.python.org/3/library/venv.html).

Naviagte to the folder (using cmd line) you wish to install the virtual environement. Some choose to have a dedicated folder for all their virtual environemtns whereas others choose to have the virtual environment in the top most folder for every project. If you need help with navigating via the cmd line

Write the following to create the virtual environment. The first venv is the name of the package, and the second venv is the name of the environment you are creating. You could therefore change this to whatever you want.

``` shell
python -m venv venv
```

To activate using Windows do:

``` shell
> venv\Scripts\activate
(venv) $_
```

To activate using mac:

``` shell
$source venv\bin\activate
(venv) $_
```

You will know you have activated it as it will say the name of your virtual environement in brackets at the start of the cmd line (in this case venv).

To deactivate it once you have finished with it, all you need to do is type the below. If you are successful, it will remove the name of your virtual environemnt from the brackets in the cmd line:

```shell
deactivate
$_
```

### Step 3 - Install Dependecies from requirements.txt

Now navigate to the folder which contains requirements.txt and type the following:

``` shell
pip install -r requirements.txt
```

This will read the requirements.txt file and automatically install everything within it

### Step 4 - Run a Local Server and Settings

We should by now have:  
[x] Created our config file  
[x] Set up a virtual environment  
[x] Activated it

All that is left is to run a local server.  
Using the cmd line, go to the folder with "manage.py" in it (the same one as requirements.txt) and type the following:

``` shell
python manage.py runserver
```

If this doesn't work and returns a secret key error, you will need to define the filepath to the settings file by doing:

``` shell
python manage.py runserver --settings=shelter.settings.local_settings
```


This will then run the Django project and it will state which port it is listening out on which is usually [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (port 8000). If you want to change the port, you can specify this when you are activating the local server. So for port 5050 you would do:

``` cmd
python manage.py runserver 5050 --settings=shelter.settings.local_settings
```

If it was successful, and there are no problems in the code preventing it from running (e.g. syntax error) you will see the below:

```shell
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

June 29, 2018 - 15:50:53
Django version 2.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

When you have finished with this you can press control + C to stop the local server. It is worth noting that if you make changes to the code and save it, whilst the local server is running, this will be automatically changed and you therefore do not need to stop the server and re-run it again.

'local_settings' is the name of the file being used for the settings and change this if you want to use a different file (which is in the same folder).If you want to create your own settings file, this can done by creating a new .py file within the settings folder. Ensure you import all from the base_settings.py file:

```python
from .base_settings import *
```

Now you can add in the specific settings you need. Note that there is a specific file for production settings in this folder.

You will likely need to make migrations too. To do this do the following:

```cmd
python manage.py makemigrations --settings=shelter.settings.local_settings
```

Potentially you may need to specify the app which requires the migrations e.g.

```cmd
python manage.py makemigrations catalog --settings=shelter.settings.local_settings
```

Or

```cmd
python manage.py makemigrations accounts --settings=shelter.settings.local_settings
```

### Step 5 (optional) - Users

To create a user for the website you can use the createsuperuser command, however to use the signup pages of the website, you need to first ensure that the email is allowed. There is a model named PermittedEmails within shelter.accounts.models. This is used to control who is able to sign up on the website. When using the sign up form, there is avalidation to ensure no one can sign up with a username or email which already exists, or an email which is not permitted; this validation is done within forms.py.

### Step 6 Test Coverage

To test your coverage, you can use coverage (pip install coverage) and following the below commands to show the % of the code which the tests cover/touch.

```cmd
coverage run --source='.' manage.py test the-app-you-want-to-test --settings=shelter.settings.local_settings
```

This will then create a coverage file in the same directory. To view the results, you can generate an html report:

```cmd
coverage html
```

This will then create a folder called htmlcov. Find the index.html file and open it in your browser!