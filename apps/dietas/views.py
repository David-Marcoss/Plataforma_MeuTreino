from django.shortcuts import render
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView,CreateView,ListView,DeleteView,DetailView
from .models import Receitas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .form import ReceitasForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q



class CreateReceitasView(LoginRequiredMixin,CreateView):
    template_name = "exercicios_form.html"
    model = Receitas
    form_class = ReceitasForm

    def get_success_url(self):
        messages.info(self.request,'Receita criada!!')
        
        return reverse_lazy('receitas')

    def form_valid(self, form):
        
        exercicio = form.save(commit=False) # salva os dados do form no bancos
        
        exercicio.categoria = form.cleaned_data['categoria']
        exercicio.user = self.request.user
        exercicio = form.save()  # salva os dados do form no banco


        return super().form_valid(form)
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Criar Receita'
        context['botao'] = 'Criar'
        context['pagina'] = 'Receitas'

        return context

class ListReceitasView(ListView):
    model = Receitas
    template_name = "refeicoes.html"
    paginate_by = 6

class UpdateReceitasView(LoginRequiredMixin,UpdateView):

    model= Receitas
    template_name = "exercicios_form.html"
    form_class = ReceitasForm

    def get_object(self):
        return get_object_or_404(Receitas,user=self.request.user,pk=self.kwargs['pk'])


    def get_success_url(self):
        messages.info(self.request,'Receita Atualizada!!')
        
        return self.request.GET.get('next',reverse_lazy('receitas'))

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Editar Receita'
        context['botao'] = 'Salvar alterações'
        context['pagina'] = 'Receitas'

        return context

class DeleteReceitasView(DeleteView):
    template_name = "exercicios_form.html"
    model =  model= Receitas
    
    def get_success_url(self):
        messages.info(self.request,'Receitas Excluida!!')
        
        return self.request.GET.get('next',reverse_lazy('receitas'))

    def get_object(self):
        return get_object_or_404(Receitas,user=self.request.user,pk=self.kwargs['pk'])
      
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Deseja Excluir a Receitas?'
        context['botao'] = 'Confirmar'
        context['pagina'] = 'Receitas'

        return context


class DetailReceitasView(DetailView):
    template_name = 'refeicao_detail.html'
    model = Receitas

class ListReceitasUserView(ListView):
    model = Receitas
    template_name = "refeicoes.html"
    paginate_by = 6

    def get_queryset(self):
        return self.request.user.receitas.all()

