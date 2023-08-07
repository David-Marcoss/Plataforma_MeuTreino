from django import forms

from apps.auxiliares.funcoes_auxiliares import trata_link, verifica_link
from .models import Receitas

class ReceitasForm(forms.ModelForm):

    categoria = forms.ChoiceField(
        choices=(('Almoço', 'Almoço'), 
                 ('Janta', 'Janta'),
                 ('Lanche', 'Lanche'),
                 ('Café da Manhã', 'Café da Manhã'), 
                 ('Lanche da manhã', 'Lanche da manhã'),
                 (' Lanche da tarde', ' Lanche da tarde'),
                 ('Ceia','Ceia'),
                 ('Outro', 'Outro')
                 ,), label='Categoria')
     
    class Meta:
        model = Receitas

        fields = ["nome","ingredientes","preparo","tempo_preparo","calorias","img","video","categoria"]
     
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
