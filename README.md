# Shelter-Record-Manager

This is a project to build an app to manage the day to day running of an animal shelter.

## How to get up and running

Before we get started the below assumes that you have python installed. This project has been created using 3.6. If you do not have python, see the [python website](https://www.python.org/downloads/) to download it.
If you have multiple versions of python installed on your computer, where it refers to typing "python" in the cmd line, you will need to specify which one you have e.g.

```
python3
```

If you are using any version of Python older than 3.4 (and that includes the 2.7 release), virtual environments are not supported natively. For those versions of Python, you need to download and install a third-party tool called virtualenv before you can create virtual environments.

### Step 1 - Create Secret Key file

All of the settings are stored within a file named "secret_environment_keys.py" which is imported into "settings.py". You will see at the top of settings.py it imports Config.

Within the shelter folder add in the following code to a file called "secret_environment_keys.py":

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
|       +--templates
|       .gitignote
|       manage.py
|       secret_environment_keys.py
+---README.md
+---requirments.txt
+---UI-notes.txt
```

### Step 2 - Create virtual Environment

This will use venv package built into [python](https://docs.python.org/3/library/venv.html).

Naviagte to the folder (using cmd line) you wish to install the virtual environement. Some choose to have a dedicated folder for all their virtual environemtns whereas others choose to have the virtual environment in the top most folder for every project. If you need help with navigating via the cmd line

Write the following to create the virtual environment. The first venv is the name of the package, and the second venv is the name of the environment you are creating. You could therefore change this to whatever you want.

``` cmd
python -m venv venv
```

To activate using Windows do:

``` cmd
> venv\Scripts\activate
(venv) $_
```

To activate using mac:

``` cmd
$source venv\bin\activate
(venv) $_
```

You will know you have activated it as it will say the name of your virtual environement in brackets at the start of the cmd line (in this case venv).

To deactivate it once you have finished with it, all you need to do is type the below. If you are successful, it will remove the name of your virtual environemnt from the brackets in the cmd line:

```cmd
deactivate
$_
```

### Step 3 - Install Dependecies from requirements.txt

Now navigate to the folder which contains requirements.txt and type the following:

``` cmd
pip install -r requirements.txt
```

This will read the requirements.txt file and automatically install everything within it

### Step 4 - Run a Local Server

We should by now have created our config file, virtual environment and activated it. All that is left is to run a local server.

Using the cmd line, go to the folder with "manage.py" in it (the same one as requirements.txt) and type the following:

``` cmd
python manage.py runserver
```

This will then run the Django project and it will state which port it is listening out on which is usually [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (port 8000). If you want to change the port, you can specify this when you are activating the local server. So for port 5050 you would do:

``` cmd
python manage.py runserver 5050
```

If it was successful, and there are no problems in the code preventing it from running (e.g. syntax error) you will see the below:

```
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