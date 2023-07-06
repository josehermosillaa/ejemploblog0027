from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Article
from .forms import ArticleForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required 
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    articulos = Article.objects.all()
    context = {'articulos':articulos}
    return render(request, 'articulos/articulos.html', context)

@login_required(login_url='/login/')
def content_view(request,id):
    articulo = Article.objects.get(id=id)  #get encuentra al unico dato que corresponda en la bd
    #si encuentra mas de uno, genera un error
    context = {'articulo': articulo}
    return render(request, 'articulos/contenido.html',context)

@login_required(login_url='/login/')
# @permission_required(perm='user.is_staff', raise_exception=True)
@staff_member_required
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


def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() #me devuelve el objeto usuario
            login(request, user)
            messages.success(request, "Se ha registrado Satisfactoriamente")
            return HttpResponseRedirect("/")
        else:
            messages.error(request,"Registro invalido, Algunos datos creados no son correctos")
        return HttpResponseRedirect("/register/")

    form = UserRegisterForm()
    context = {'form':form}
    return render(request, 'articulos/registro.html',context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) #si existe -> object user
            #si no existe ->None
            if user is not None:
                login(request, user)
                messages.info(request, f'Iniciaste sesion como {username}.')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Nombre de ususario y/o contraseña incorrecta')
                return HttpResponseRedirect('/login/')
        else:
            messages.error(request, 'Nombre de ususario y/o contraseña incorrecta')
            return HttpResponseRedirect('/login/')
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'articulos/login.html',context)

def logout_view(request):
    logout(request)
    messages.info(request, "se ha cerrado la sesion correctamente")
    return HttpResponseRedirect('/login/')