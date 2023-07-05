from django import forms

#Importar el modelo Article
from .models import Article

# crear Formulario con ModelForm

class ArticleForm(forms.ModelForm):
    #Especificar el modelo que tomaremos como referencia a traves de los Metadatos 
    class Meta:
        model = Article
        fields = "__all__"