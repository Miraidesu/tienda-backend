from django.shortcuts import render, get_object_or_404
from tienda.models import Componente, TipoComponente

def index(request):
    return render(request, "index.html")

def lista_componentes(request, categoria):
    if categoria == "todo":
        comp = Componente.objects.all()
    else:
        cat = get_object_or_404(TipoComponente, nombre=categoria)
        comp = Componente.objects.filter(tipo=cat)

    context = {"componentes": comp}
    return render(request, "listado.html", context)

def detalle_componente(request, id):
    comp = Componente.objects.get(id=id)
    context = {"componente": comp}
    return render(request, "detalle.html", context)