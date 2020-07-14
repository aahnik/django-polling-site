# django-polling_site
django-polling_site

# THE SCRIPTs ARE TO BE RUN FROM DJANGO SHELL 

> inside apps you can't write your own scripts because they are run by django. Running a module directly will give lots of import errors

_YOU WILL GET ERRORS IF YOU RUN THESE SCRIPT IN CWD CONTEXT_

DON'T RUN DIRECTLY LIKE 
```shell
python3 script.py
```

## The `exec()` Function 

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