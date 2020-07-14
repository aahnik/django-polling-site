# THE SCRIPTs ARE TO BE RUN FROM DJANGO SHELL 

> DOING SOME TASKS ARE EXTREMELY DIFFICULT INSIDE APPS 
> BEACUSE OF IMPORT ERRORS
> AND POPULATING DATABASE NOT WORKING INSIDE TESTS ..


## _YOU WILL GET ERRORS IF YOU RUN THIS SCRIPT IN CWD CONTEXT_

DON'T RUN DIRECTLY LIKE 
```shell
python3 populate.py
```

1. START THE DJANGO CONTEXT BY RUNNING 

```shell
$ python3 manage.py shell
```
2. EXECUTE THE SCRIPT IN PYTHON CONSOLE RUNNING IN DJANGO CONTEXT 

```
>>> exec(open('script.py').read())
```

# OR 

RUN an arbitrary set of python commands within the DJANGO CONTEXT  
It offers the same usability and functionality 
as running a set of commands in django shell

```shell
$ python manage.py runscript script.py
```    
