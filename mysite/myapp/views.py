from .models import Task
from django.shortcuts import render,redirect
from .forms import TodoForm
from django.views.generic import ListView

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'myapp/index.html'
    context_object_name = 'task_list'

    

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name,priority=priority,date=date)
        task.save()
        return redirect('/')
    task_list = Task.objects.all()

    return render(request,'myapp/index.html', {'task_list':task_list})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'myapp/delete.html', {'task':task})


def update(request, id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/edit.html', {'form':form})

