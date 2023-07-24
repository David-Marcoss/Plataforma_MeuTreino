from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView,CreateView,ListView,DeleteView,DetailView
from .models import Exercicios
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .form import ExerciciosForm



def treinosView(request):      
    return render(request,template_name='treinos.html')

class CreateExercicioView(LoginRequiredMixin,CreateView):
    template_name = "exercicios_form.html"
    model = Exercicios
    form_class = ExerciciosForm

    def get_success_url(self):
        messages.info(self.request,'Exercicio criado!!')
        
        return reverse_lazy('exercicios-user')

    def form_valid(self, form):
        
        exercicio = form.save(commit=False) # salva os dados do form no bancos
        
        exercicio.categoria = form.cleaned_data['categoria']
        exercicio.user = self.request.user
        exercicio = form.save()  # salva os dados do form no banco


        return super().form_valid(form)
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Criar Exercicio'
        context['botao'] = 'Criar'

        return context

class ListExerciciosView(ListView):
    model = Exercicios
    template_name = "exercicios.html"
    paginate_by = 16


class UpdateExerciciosView(LoginRequiredMixin,UpdateView):

    model= Exercicios
    template_name = "exercicios_form.html"
    form_class = ExerciciosForm

    def get_object(self):
        return get_object_or_404(Exercicios,user=self.request.user,pk=self.kwargs['pk'])


    def get_success_url(self):
        messages.info(self.request,'Exercicio Atualizado!!')
        
        return self.request.GET.get('next',reverse_lazy('exercicios'))

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Editar Exercicio'
        context['botao'] = 'Salvar alterações'

        return context

class DeleteExerciciosView(DeleteView):
    template_name = "exercicios_form.html"
    model =  model= Exercicios
    
    def get_success_url(self):
        messages.info(self.request,'Exercicio Excluido!!')
        
        return self.request.GET.get('next',reverse_lazy('exercicios'))

    def get_object(self):
        return get_object_or_404(Exercicios,user=self.request.user,pk=self.kwargs['pk'])
      
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Deseja Excluir o Exercício?'
        context['botao'] = 'Confirmar'

        return context
    

class ListExerciciosUserView(ListView):
    model = Exercicios
    template_name = "exercicios.html"
    paginate_by = 16

    def get_queryset(self):
        return self.request.user.exercicios.all()

class DetailExerciciosView(DetailView):
    template_name = 'exercicios_detail.html'
    model = Exercicios

    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        ex = Exercicios.objects.get(pk=self.kwargs['pk'])

        context['object_list'] = Exercicios.objects.filter(categoria = ex.categoria).exclude(pk = ex.pk)[:4]

        return context
