# to_do_list
We are using python 3.5 and Django 2.0.6

Switch on the virtual envirement for python 3.5 and do the following
Step 1: install all the requirements using requirements.txt file using the command
```
pip install -r requirements.txt
```
Step 2: Run the migrations by using the command
```
python manage.py migrate
```
Step 3: Run the server by using the command
```
python manage.py runserver
```

The links for the the app are
```
http://localhost:8000/ 
```
for the list of all todos
```
http://localhost:8000/add 
```
to add a todo

The APi endpoints to list all the todos is
```
http://localhost:8000/api/todo/list 
```
```
http://localhost:8000/api/todo/<id> 
``` 
to show all the details one todo
