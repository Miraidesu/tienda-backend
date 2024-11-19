from django.shortcuts import render
from tienda.models import Componente

class Carrito:
    def __init__(self, listado: list = []) -> None:
        self.listado = listado

    def agregar(self, producto: dict) -> bool:
        if producto["id"] and producto["cantidad"]:
            self.listado.append(producto)
            return True
        return False

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

carrito = Carrito([{ "id": 1, "cantidad": 2 }])

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

def carrito_compras(request):
    context = {"carrito": carrito.ver_carrito()}
    print(context)
    return render(request, "carrito.html", context)