from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import CreateView, DeleteView


class TaskCreate(CreateView):
  model = Task
  fields = '__all__'
  success_url = '/'

class TaskDelete(DeleteView):
  model = Task
  success_url = '/'


def tasks_index(request):
  tasks = Task.objects.all()
  return render(request, 'tasks/index.html', { 'tasks': tasks })

def home(request):
  return render(request, 'home.html')



def tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST) 
        if form.is_valid():
            form.save() 
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)



