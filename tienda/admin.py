from django.contrib import admin
from .models import Componente, TipoComponente, Venta, DetalleVenta

class ComponenteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'tipo', 'imagen')

class DetalleVentaAdmin(admin.ModelAdmin):
	list_display = ('venta', 'componente', 'cantidad', 'subtotal')

admin.site.register(Componente, ComponenteAdmin)
admin.site.register(TipoComponente)
admin.site.register(Venta)
admin.site.register(DetalleVenta, DetalleVentaAdmin)
