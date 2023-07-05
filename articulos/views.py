from django.shortcuts import render, HttpResponse
from .models import Article
# Create your views here.

def index(request):
    articulos = Article.objects.all()
    context = {'articulos':articulos}
    return render(request, 'articulos/articulos.html', context)

def content_view(request,id):
    articulo = Article.objects.get(id=id)  #get encuentra al unico dato que corresponda en la bd
    #si encuentra mas de uno, genera un error
    context = {'articulo': articulo}
    return render(request, 'articulos/contenido.html',context)