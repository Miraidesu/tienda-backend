from django.contrib import admin
from .models import Componente, TipoComponente

class ComponenteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'tipo', 'imagen')

admin.site.register(Componente, ComponenteAdmin)
admin.site.register(TipoComponente)