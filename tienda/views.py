from django.shortcuts import render, redirect
from tienda.models import Componente, Venta, DetalleVenta

def iniciar_sesion(request):
    request.session['usuario'] = "admin"
    request.session['carrito'] = []

    return redirect("index")

def cerrar_sesion(request):
    del request.session['usuario']
    del request.session['carrito']

    return redirect("index")

def index(request):
    comp = Componente.objects.all()[:4]
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
    carrito = request.session['carrito']

    detalle_carrito = []
    total = 0
    lista_comp = Componente.objects.all()

    for comp in lista_comp:
        comp_carr = [p for p in carrito if p["id"] == comp.id]
        if comp_carr:
            subtotal = comp_carr[0]["cantidad"] * comp.precio
            detalle_carrito.append({
                "producto": comp,
                "cantidad": comp_carr[0]["cantidad"],
                "subtotal": subtotal
            })
            total += subtotal

    context = {"carrito": detalle_carrito, "total": total}

    return render(request, "carrito.html", context)

def agregar_carrito(request, id):
    if request.method == "POST":
        carrito = request.session['carrito']
        cantidad = int(request.POST.get("cantidad"))

        for c in carrito:
            if c["id"] == id:
                c["cantidad"] = cantidad
                request.session['carrito'] = carrito
                return redirect("carrito_compras")

        carrito.append({ "id": id, "cantidad": cantidad })
        request.session['carrito'] = carrito

        return redirect("carrito_compras")
    
    return redirect("detalle_componente", id=id)

def pagar(request):
    carrito = request.session['carrito']
    total = 0
    lista_comp = Componente.objects.all()

    for comp in lista_comp:
        comp_carr = [p for p in carrito if p["id"] == comp.id]
        if comp_carr:
            total += comp_carr[0]["cantidad"] * comp.precio

    venta = Venta(total=total)
    venta.save()

    for comp in lista_comp:
        comp_carr = [p for p in carrito if p["id"] == comp.id]
        if comp_carr:
            comp.stock -= comp_carr[0]["cantidad"]
            comp.save()

            detalle = DetalleVenta(
                componente=comp,
                cantidad=comp_carr[0]["cantidad"],
                subtotal=comp_carr[0]["cantidad"] * comp.precio,
                venta=venta
            )
            detalle.save()
            
    request.session['carrito'] = []
    return redirect("index")