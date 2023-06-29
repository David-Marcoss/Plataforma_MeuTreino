from django.contrib.auth.forms import UserCreationForm,UserChangeForm

#from accounts.models import User
from django.contrib.auth import get_user_model

from django import forms

#para personalizar formularios cria-se uma arquivo form para sobrescreber ou criar formularios
#este arquivo vai servir para personalizar o user padrao do django

User = get_user_model() 


#form para cadastro de usuario
class UserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
    
    #definição de valores padrao
    class Meta:
        model = User  # model padrao de usuarios do django
        fields = ['username', 'nome','email']


class UserChangeForm(UserChangeForm):

    #definição de valores padrao
    class Meta:
        model = User  # model padrao de usuarios do django
        fields = ['imageperfil','nascimento','altura', 'peso','sexo']



'''

"""
    Form para redefinição de senha, onde o usuario
    deve digitar seu e-mail para recuperar senha
"""
class Redefinir_senhaForm(forms.Form):

    email = forms.EmailField(label='E-mail')


    def clean_email(self):

        email = self.cleaned_data['email']

        if User.objects.filter(email = email).exists():
            return email
        else:
            raise forms.ValidationError('E-mail não cadastrado!!') 

    def save(self):

        usuario = User.objects.get(email=self.cleaned_data['email'])    
        key = generate_hash_key(usuario.username)

        reset = redefinir_senha(User = usuario,key = key) 
        #salva os dados no banco e armazena o horario em que a key foi gerada
        reset.save()

        #define o tempo em que a key é valida que de 1h
        time = acesentar_tempo(reset.horario)
        reset.expira_em = time 

        reset.save()
        

        template_name = 'account/reset_password.html'
        assunto = "Instruções para redefinir senha"
        context = {'reset':reset}

        send_mail_template(assunto,template_name,context,[usuario.email])

'''
