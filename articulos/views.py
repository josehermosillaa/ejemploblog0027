from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
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

def create_article_view(request):
    if request.method == 'POST':
        #crear una instancia del formulario con los datos que se enviaron
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"se ha agregado el articulo correctamente")
            return HttpResponseRedirect("/")
    form = ArticleForm()
    context = {
        'form':form
    }
        
    return render(request, 'articulos/formulario.html', context)