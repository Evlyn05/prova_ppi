from django.shortcuts import render, redirect
from .models import Voo
from .forms import VooForm


# Create your views here.
def index(request):
    voos = Voo.objects.all()
    contexto = {
        'voos': voos
    }
    return render(request,'core/index.html',contexto)

def lista(request):
    voos = Voo.objects.all()
    contexto = {
        'voos': voos
    }
    return render(request,'core/lista.html',contexto)


def cadastro(request):
    form = VooForm()
    if request.method == 'POST':
        form = VooForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_voo')
        
        form = VooForm()
    contexto={
             'form': form
    }  
    return render(request,'core/form.html',contexto)

def editar_voo(request,id):
    voo = Voo.objects.get(id=id)

    if request.method == 'POST':
        form = VooForm(request.POST,instance=voo)
        if form.is_valid():
            form.save()
            return redirect('lista_voo')
    else:
        form = VooForm(instance=voo)

    contexto={
            'form':form
    }
    return render(request,'core/form.html',contexto)
        
def remover_voo(request,id):
    voo = Voo.objects.get(id=id)
    voo.delete()
    return redirect('lista_voo')

    

