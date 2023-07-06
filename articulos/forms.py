from django import forms

#Importar el modelo Article
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# crear Formulario con ModelForm

class ArticleForm(forms.ModelForm):
    #Especificar el modelo que tomaremos como referencia a traves de los Metadatos 
    class Meta:
        model = Article
        fields = "__all__"

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1","password2")