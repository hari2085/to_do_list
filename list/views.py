from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from . models import *
from django.http import JsonResponse

def TodoList(request):
	todos = Todo.objects.all()

	context = {

		'todos' : todos,
	}

	return render(request,'todo_list.html',context)

def Delete(request,todo_id):
	del_obj = get_object_or_404(Todo,id = todo_id).delete()
	return redirect('/')

def Add(request):
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save()
			return redirect('/')
	else:
		form = TodoForm()

	context = {

		'form' : form,
	}

	return render(request,'add.html',context)

def Edit(request, todo_id):
	edit_obj = get_object_or_404(Todo,id = todo_id)
	if request.method == 'POST':
	
		title = request.POST.get('title')
		description = request.POST.get('description')
		status = request.POST.get('status')

		edit_obj.title = title
		edit_obj.description = description
		edit_obj.status = status

		edit_obj.save()
		return redirect('/')
	else:
		form = TodoForm()
	context = {

		'form' : form,
		'edit_obj':edit_obj,
	}

	return render(request,'edit.html',context)

def TodoListApi(request):
	todos = Todo.objects.all()

	data = {"todo_list": list(todos.values("id", "time_created", "title","description","status"))}
	return JsonResponse(data)

def TodoDetail(request,todo_id):
	todo = get_object_or_404(Todo,id = todo_id)

	data = {"todo": {"id":todo.id, "time_created": todo.time_created, "title":todo.title, "description":todo.description,"status":todo.status}}
	return JsonResponse(data)
