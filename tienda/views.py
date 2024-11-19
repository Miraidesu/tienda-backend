from django.shortcuts import render, get_object_or_404
from tienda.models import Componente, TipoComponente

def index(request):
    return render(request, "index.html")

def lista_componentes(request):
    comp = Componente.objects.all()

    context = {"componentes": comp}
    return render(request, "listado.html", context)

def detalle_componente(request, id):
    comp = Componente.objects.get(id=id)
    context = {"componente": comp}
    return render(request, "detalle.html", context)