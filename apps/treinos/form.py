from django import forms

from apps.auxiliares.funcoes_auxiliares import trata_link, verifica_link
from .models import Exercicios


class ExerciciosForm(forms.ModelForm):

    categoria = forms.ChoiceField(
        choices=(('Perna', 'Perna'), 
                 ('Peito', 'Peito'),
                 ('Costas', 'Costas'),
                 ('Bisceps', 'Bisceps'), 
                 ('Trisceps', 'Trisceps'),
                 ('Antebraço', 'Antebraço'),
                 ('Quadriceps', 'Quadriceps'), 
                 ('Posterior coxa', 'Posterior coxa'),
                 ('Abdominal', 'Abdominal'),
                 ('ABS', 'ABS'),
                 ('Powerlifting', 'powerlifting'), 
                 ('Calistenia', 'calistenia'),
                 ('Outro', 'Outro')
                 ,), label='Categoria')
     
    class Meta:
        model = Exercicios

        fields = ["nome","num_series","num_repeticoes","descanco","img","video","descricao","categoria"]
     
     #função para validação do campo video
    def clean_video(self):
        
        if self.cleaned_data['video']:
            if verifica_link(self.cleaned_data['video']):
                video = self.cleaned_data['video']
                video = trata_link(video)
                
                return video
            else:
                raise forms.ValidationError('Por favor, digite um link valido!!')
        return '' 

