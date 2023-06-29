from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm  #form padrao para alteração de senha
from django.contrib.auth import authenticate,login #metodos de login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

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


class cadastroview2(UpdateView):
    model= User
    template_name = 'cadastro.html'

    fields = ['imageperfil','nascimento','altura', 'peso','sexo']

    success_url = reverse_lazy('home') 

    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        
        context['titulo'] = 'Informações Complementares'
        context['texto'] = 'Informe seus dados para concluir os cadastro na nossa plataforma.'
        context['botao'] = 'Finalizar cadastro'

        return context