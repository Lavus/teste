from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.utils import timezone
from .models import *
from .forms import *
from .classe_auxiliar import handle_uploaded_file
import json
from django.views.decorators.csrf import csrf_exempt
from cloudinary.forms import cl_init_js_callbacks
from cloudinary import api # Only required for creating upload presets on the fly
import cloudinary.uploader
from django.contrib.auth.models import User

def filter_nones(d):
    if d and d !=0:
        return dict((k,v) for k,v in d.items() if v is not None)

def listar(tipo):
    defaults = dict(format="jpg", height=150, width=150)
    defaults["class"] = "thumbnail inline"

    # The different transformations to present
    samples = [
        dict(crop="fill", radius=10),
        dict(crop="scale"),
        dict(crop="fit", format="png"),
        dict(crop="thumb", gravity="face"),
        dict(format="png", angle=20, height=None, width=None, transformation=[
            dict(crop="fill", gravity="north", width=150, height=150, effect="sepia"),
        ]),
    ]
    samples = [filter_nones(dict(defaults, **sample)) for sample in samples]
    if tipo == "imovel":
        objetos = Imagem.objects.all()
    elif tipo == "depoimento":
        objetos = Depoimento.objects.all()
    elif tipo == "destaque":
        objetos = Destaque.objects.all()
    return (dict(photos=objetos, samples=samples))

def list_imovel(request):
    if request.method == 'POST':
        if 'apagar' in request.POST:
            apagar = Imagem.objects.get(pk=request.POST['id_photo'])
            cloudinary.uploader.destroy(apagar.imagem.public_id,invalidate=True)
            apagar.delete()
    dicionario = listar("imovel")
    return render(request, 'blog/list_imovel.html', dicionario)

def list_depoimento(request):
    if request.method == 'POST':
        if 'apagar' in request.POST:
            apagar = Depoimento.objects.get(pk=request.POST['id_photo'])
            cloudinary.uploader.destroy(apagar.imagem.public_id,invalidate=True)
            apagar.delete()
    dicionario = listar("depoimento")
    return render(request, 'blog/list_depoimento.html', dicionario)

def list_destaque(request):
    if request.method == 'POST':
        if 'apagar' in request.POST:
            apagar = Destaque.objects.get(pk=request.POST['id_photo'])
            cloudinary.uploader.destroy(apagar.imagem.public_id,invalidate=True)
            apagar.delete()
    dicionario = listar("destaque")
    return render(request, 'blog/list_destaque.html', dicionario)

def upload(tipo,dados):
    if tipo == "imovel":
        backend_form = ImagemForm()
    elif tipo == "depoimento":
        backend_form = DepoimentoForm()
    elif tipo == "destaque":
        backend_form = DestaqueForm()
    context = dict(
        backend_form = backend_form,
        posted = []
    )
    if dados.method == 'POST':
        if tipo == "imovel":
            form = ImagemForm(dados.POST, dados.FILES)
        elif tipo == "depoimento":
            form = DepoimentoForm(dados.POST, dados.FILES)
        elif tipo == "destaque":
            form = DestaqueForm(dados.POST, dados.FILES)
        if form.is_valid():
            if tipo == "imovel":
                album = Imovel.objects.get(pk=dados.POST['album'])
                new = Imagem(titulo=dados.POST['titulo'], album=album, imagem=dados.FILES['imagem'])
            elif tipo == "depoimento":
                autor = User.objects.get(pk=dados.POST['autor'])
                new = Depoimento(titulo=dados.POST['titulo'], descricao=dados.POST['descricao'], autor=autor, imagem=dados.FILES['imagem'])
            elif tipo == "destaque":
                autor = User.objects.get(pk=dados.POST['autor'])
                new = Destaque(titulo=dados.POST['titulo'], descricao=dados.POST['descricao'], autor=autor, imagem=dados.FILES['imagem'])
            new.publish()
        else:
            erro = form.errors.as_data()
            for key in erro.keys():
                erro = erro[key]
                erro = erro[0]
                erro = erro.message
                context['posted'].append(erro)
    return (context)

def upload_imovel(request):
    contexto = upload('imovel', request)
    return render(request, 'blog/upload_imovel.html', contexto)

def upload_depoimento(request):
    contexto = upload('depoimento', request)
    return render(request, 'blog/upload_depoimento.html', contexto)

def upload_destaque(request):
    contexto = upload('destaque', request)
    return render(request, 'blog/upload_destaque.html', contexto)

def index(request):
    imoveis = Imovel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    destaques = Destaque.objects.all()
    imagens = Imagem.objects.all()
    context = {'imoveis':imoveis, 'destaques':destaques, 'imagens':imagens}
    return render(request, 'blog/index.html', context)

def imovel_info(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk) #Imovel.objects.get(pk=pk)
    return render(request, 'blog/imovel_info.html', {'imovel': imovel})

def destaques(request):
    destaques = Destaque.objects.all()
    return render(request, 'blog/index.html',{'destaques':destaques})

def depoimentos(request):
    depoimentos = Depoimento.objects.all()
    return render(request, 'blog/index.html',{'depoimentos':depoimentos})
