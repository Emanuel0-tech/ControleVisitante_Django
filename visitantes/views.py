<<<<<<< HEAD
from django.shortcuts import redirect, render
from django.contrib import messages
from visitantes.forms import VisitanteForm
from django.contrib.auth.decorators import login_required

@login_required
def registrar_visitante(request):
    form = VisitanteForm()
    
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        
        if form.is_valid():
            visitante = form.save(commit=False)
            
            visitante.registrado_por = request.user.porteiro
            visitante = form.save()
            
            messages.success(request,'Visitante registrado com sucesso')
            return redirect('index')
        
    context ={
        'nome_pagina': 'Registrar visitante',
        'form': form
    }
    
    return render(request,'registrar_visitante.html',context)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 259bea34cf67988f3aafeb19514fc5d39454096e
