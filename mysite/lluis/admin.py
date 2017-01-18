from django.contrib import admin


from .models import Usuarios
from .models import Productos
from .models import Ticket


admin.site.register(Ticket)

class UsuariosAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,			{'fields': ['password']}),
	('Informacion User', {'fields': ('nombreusuario','nombre','apellidos','fechanacimiento','telefono')})
	]
	list_display = ('nombreusuario','nombre','apellidos','fechanacimiento','telefono')
	list_filter = ['fechanacimiento']
admin.site.register(Usuarios, UsuariosAdmin)

class ProductosAdmin(admin.ModelAdmin):
	fieldsets = [
	('Informacion Producto', {'fields': ('nombreproductos','cantidad','precioproducto','categoria')})
	]
	list_display = ('nombreproductos','cantidad','precioproducto','categoria')
	list_filter = ['categoria']
admin.site.register(Productos, ProductosAdmin)
# Register your models here.
