from typing import Any
from django import forms
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView,CreateView,ListView,DeleteView,DetailView
from .models import Exercicios,Treinos,Exercicios_do_treino
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .form import ExerciciosForm,TreinosForm,ExerciciosTreinoForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q



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
        context['pagina'] = 'Exercicios'

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
        context['pagina'] = 'Exercicios'

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


@login_required
def CreateTreinoView(request):
    template_name = "exercicios_form.html"

    if request.method == 'POST': 
        form = TreinosForm(request.POST, request.FILES)

        if form.is_valid(): 
            treino = form.save(commit=False)
            treino.categoria = form.cleaned_data['categoria']
            treino.user = request.user
            treino = form.save()  # salva os dados do form no banco

            return redirect('treinos-create-exercicios',pk=int(treino.id))
    
    else:
        form = TreinosForm()


    context = {}

    context['titulo'] = 'Criar Treino'
    context['botao'] = 'Criar'
    context['pagina'] = 'Treinos'
    context['form'] = form

    return render(request,template_name,context)

@login_required
def CreateExerciciosTreino(request,pk):
    template_name = "exercicios_treino.html"
    treino = Treinos.objects.get(pk=pk)

    if request.method == 'POST': 
        form = ExerciciosTreinoForm(request.POST, request.FILES)

        if form.is_valid(): 
            
            object = form

            for exercicios in object.cleaned_data['exercicio']:
                print(exercicios)
                ex = Exercicios.objects.get(pk=exercicios)
                Exercicios_do_treino.objects.create(exercicio=ex,treino=treino)
            
            
            return redirect('treinos')
    
    else:
        busca = request.GET.get("Busca")

        if busca:
            values = busca.split()
            object_list = []
            
            for busca in values:    
                if len(busca) > 2:
                    object_list += Exercicios.objects.filter(
                        Q(nome__icontains = busca ) | Q(categoria__icontains = busca ) )  

            object_list = set(object_list) 
            
            choices = []
            
            for i in object_list:
                choices.append((i.id,i))
            
            form = ExerciciosTreinoForm()
            form.fields['exercicio'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            choices=choices,label="Exercicios")
        else:
            form = ExerciciosTreinoForm()



    context = {}

    context['titulo'] = 'Adcionar Exercicios'
    context['botao'] = 'Salvar'
    context['treino'] = treino
    context['form'] = form

    return render(request,template_name,context)

    
class ListTreinosView(ListView):
    model = Treinos
    template_name = "treinos.html"
    paginate_by = 6

class ListTreinosUserView(ListView):
    model = Treinos
    template_name = "treinos.html"
    paginate_by = 6

    def get_queryset(self):
        return self.request.user.treinos.all()