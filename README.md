# django-polling_site
django-polling_site ( Life's First Django Project)

[**SEE SCREENSHOTS**](https://github.com/aahnik/django-polling_site/tree/master/ScreenShots)

## HOW TO RUN IN YOUR COMPUTER

__pre-requisites : python(3.8 or above) and pip must be installed__ 



**1. CREATE AND ACTIVATE A VIRTUAL ENVIRONMENT INSIDE A NEW DIRECTORY**

Virtual Environments are a great way to wrap python projects. I have stopped working on this repo on Jul 15 2020. At the time of my work I have used the latest versions of python and django. If you are reading this after 2020, chances are new versions of python and django might have rolled out . So to ensure that old code runs smoothly , create a virtual environment. 

*Using Virtual Environments ensures the dependancies of each project is independently availaible and there is no headache of breakage of code and EVERY PROJECT STAYS INDEPENDENT OF ONE ANOTHER* 
IF YOU ARE NEW TO VIRTUAL ENVIRONMENTS READ [PYTHON-3 OFFICIAL DOCS](https://docs.python.org/3/library/venv.html) 

**2. CLONE THIS REPO `django-polling-site` IN YOUR DIRECTORY, AND INSTALL THE REQUIREMENTS**

`pip install -r requirements.txt`

**3. MOVE INSIDE THE `pollsite` DIRECTORY AND MAKE MIGRATIONS**

`python manage.py makemigrations`

`python manage.py migrate`

**4. CREATE A SUPERUSER , WITH YOUR OWN USERNAME AND PASSWORD**

`python manage.py createsuperuser`

**5. POPULATE DATABASE WITH DUMMY DATA OF QUESTIONS AND CHOICES, BY RUNNING THE `populator_script` FROM DJANGO SHELL**

[click here to see how](https://github.com/aahnik/django-polling_site#running-scripts-from-django-shell)

**NOW RUN THE SERVER**

`python manage.py runserver`

Go to  http://127.0.0.1:8000/ . This is where Django starts server by default

**HOLA !! ENJOY YOU HAVE SUCCESSFULLY RUN THE SERVER**

Click on Admin button on top right corner to go the the Django Administration page.
You can add team members , change or add questions and choices


*Vist DJANGO'S OFFICIAL WEBSITE FOR MORE DETAILS..*

__you can now play around with the code your self__


## RUNNING SCRIPTs FROM DJANGO SHELL 

> inside apps you can't write your own scripts because they are run by django. Running a module directly will give lots of import errors

_YOU WILL GET ERRORS IF YOU RUN THESE SCRIPT IN CWD CONTEXT_

DON'T RUN DIRECTLY LIKE 

```shell
python3 script.py
```

**The `exec()` Function**

`exec()` function is used for the dynamic execution of Python program 
which can either be in form of a  string or object code. If it is a **string**, 
the _string is parsed as a suite of Python statements_ which is then executed
 _unless a syntax error occurs_ and if it is an object code, it is simply executed.

1. START THE **DJANGO SHELL**  BY RUNNING 

```shell
$ python3 manage.py shell
```
(because Django Shell offers special access features)

2. LOAD THE SCRIPT IN A VARIABLE

```shell
>>> script = open(script_path).read()
```

3. EXECUTE THE SCRIPT IN PYTHON CONSOLE RUNNING IN DJANGO CONTEXT 

```
>>> exec(script)
```
