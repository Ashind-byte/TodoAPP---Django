from django.shortcuts import redirect, render

from .models import TodoModel
from .forms import TodoForm

# Create your views here.
def home(request):
    todos = TodoModel.objects.all()
    forms = TodoForm()
    if request.method == 'POST':
        forms = TodoForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('home')
    else:
        forms = TodoForm()

    return render(request,'index.html',{"forms":forms,'todos':todos})

def update(request,pk):
    todo = TodoModel.objects.get(id=pk)
    forms = TodoForm(instance=todo)
    if request.method =='POST':
        forms = TodoForm(request.POST,instance=todo)
        if forms.is_valid():
            forms.save()
        return redirect('home')
    else:
        forms = TodoForm(instance=todo)

    
    return render(request,'update.html',{"todos":todo,"form":forms})



def delete_todo(request,pk):

    todo = TodoModel.objects.get(id=pk)
    if request.method =='POST':
        todo.delete()
        return redirect("home")
    else:
        pass
    return render(request,'delete.html',{'todos':todo})
    