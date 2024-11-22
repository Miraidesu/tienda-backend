from django.shortcuts import render, redirect
from tienda.models import Componente

class Carrito:
    def __init__(self, listado=None) -> None:
        if listado is None:
            listado = []  # Crear una lista nueva por defecto
        self.listado = listado

    def agregar(self, producto: dict) -> bool:
        self.listado.append(producto)
        print(self.listado)

    def quitar(self, id: int) -> bool:
        for p in self.listado:
            if p["id"] == id:
                self.listado.remove(p)
                return True
        return False
    
    def vaciar(self) -> None:
        self.listado = []

    def ver_carrito(self) -> list:
        detalle_carrito = []
        lista_comp = Componente.objects.all()
        
        if not self.listado:
            return detalle_carrito

        for comp in lista_comp:
            comp_carr = [p for p in self.listado if p["id"] == comp.id]
            if comp_carr:
                detalle_carrito.append({
                    "producto": comp,
                    "cantidad": comp_carr[0]["cantidad"]
                })
        print(detalle_carrito)
        return detalle_carrito

    def esta_comp_en_carrito(self, id) -> bool:
        for c in self.listado:
            if c["id"] == id:
                return True
        return False
    
carrito = Carrito()

def index(request):
    comp = Componente.objects.all().order_by("?")[:4]
    context = {"componentes": comp}

    return render(request, "index.html", context)

def lista_componentes(request):
    comp = Componente.objects.all()

    context = {"componentes": comp}
    return render(request, "listado.html", context)

def detalle_componente(request, id):
    comp = Componente.objects.get(id=id)
    context = {"componente": comp}
    return render(request, "detalle.html", context)

def carrito_compras(request):
    context = {"carrito": carrito.ver_carrito()}
    print(context)
    return render(request, "carrito.html", context)

def agregar_carrito(request, id):
    if request.method == "POST":
        cantidad = int(request.POST.get("cantidad"))
        if not carrito.esta_comp_en_carrito(id):
            return redirect("detalle_componente", id=id)
        
        carrito.agregar({"id": id, "cantidad": cantidad})

        return redirect("detalle_componente", id=id)
    
    return redirect("detalle_componente", id=id)