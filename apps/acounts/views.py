from typing import Any, Optional, Type
from django.db import models
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, TemplateView
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm  #form padrao para alteração de senha
from django.contrib.auth import authenticate,login #metodos de login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserCreationForm,UserChangeForm

from .models import User,redefinir_senha
from django.contrib import messages

# Create your views here.
def cadastroview(request):
    if not request.user.is_authenticated: 
        template_name = "cadastro.html"

        if request.method == 'POST': 
            form = UserCreationForm(request.POST, request.FILES)

            if form.is_valid(): 
                user = form.save() 
                
                user = authenticate(username = user.username,password = form.cleaned_data['password1'])
                
                login(request,user)
                
                messages.info(request,"Cadastro concluido com Sucesso !!!")
                
                return redirect('cadastro-user2',pk=request.user.id)
        
        else:
            form = UserCreationForm()


        context = {}

        context['titulo'] = 'Registre-se'
        context['texto'] = 'Registre-se para acessar os recursos de nossa plataforma.'
        context['botao'] = 'Proximo'
        context['form'] = form

        return render(request,template_name,context)


class cadastroview2(LoginRequiredMixin,UpdateView):

    model= User
    template_name = 'cadastro.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('home')
    
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        
        context['titulo'] = 'Informações Complementares'
        context['texto'] = 'Informe seus dados para concluir os cadastro na nossa plataforma.'
        context['botao'] = 'Finalizar cadastro'

        return context

class perfilview(LoginRequiredMixin,UpdateView):

    model= User
    template_name = 'perfil.html'
    fields = ['nome','email','imageperfil','nascimento','altura', 'peso','sexo']
    
    def get_success_url(self):
        messages.info(self.request,'Alterações salvas com sucesso!!')
        
        return self.request.GET.get('next', reverse_lazy('home'))

class UpdatePasswordView(LoginRequiredMixin,UpdateView):

    model= User
    template_name = 'cadastro.html'
    success_url = reverse_lazy('logout')
    
    def get_form(self, form_class= None):
        form = PasswordChangeForm(data= self.request.POST, user=self.request.user)
        return form    
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        
        context['titulo'] = 'Redefinição de senha'
        context['texto'] = 'Informe uma nova senha.'
        context['botao'] = 'Salvar'

        return context