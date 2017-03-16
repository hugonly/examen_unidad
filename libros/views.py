from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Libros


# Create your views here.

def home(request):

    context=locals();
    template='home.html'
    return render(request,template,context)

def lista_libros(request):
    lib = Libros.objects.all()
    print request
    m = "Libros registrados actualmente"
    template = "listaDeLibros.html"
    contexto = {"mensaje": m,
                "libros": lib}
    return render(request, template, contexto)

def detalle_libro(request, object_id=None):

    lib = get_object_or_404(Libros, id = object_id)
    mens = "Libros registrados actualmente"
    template = "detalle_libro.html"
    contexto = {"Mensaje":mens,
                "Libros": lib}
    return render(request, template, contexto)
