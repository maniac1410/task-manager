from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

# Create your views here.

@login_required
def index(request):
    get_all_tasks = Task.objects.filter(user= request.user)
    return render(request,"tasks.html",{"tasks":get_all_tasks})


@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("tasks")
    
    else:
        form = TaskForm()

    return render(request, 'add-task.html',{"form":form})

@login_required
def edit_task(request,pk):
    task = get_object_or_404(Task, pk=pk, user = request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request,'edit-task.html', {'form':form})

@login_required
def delete_task(request, pk ):
    task = get_object_or_404(Task, pk=pk , user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("tasks")
    

    return render(request, 'delete-task.html', {'task':task})


    