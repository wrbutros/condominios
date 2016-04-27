from django.contrib import admin
from .models import Ciudad, Comuna

 ##  ====== CIUDAD =======
 class CiudadAdmin(admin.ModelAdmin):
     model = Ciudad
     list_display = ('nombre',)
     list_filter = ('nombre',)  # hay que filtrar ciudad
     search_fields = ('nombre',)


 ##  ====== COMUNA =======
 class ComunaAdmin(admin.ModelAdmin):
     model = Comuna
     list_display = ('nombre', 'get_nombre_ciudad')
     list_filter = ('nombre',)  # hay que filtrar ciudad
     search_fields = ('nombre', 'get_nombre_ciudad')

     def get_nombre_ciudad(self, obj):
         return obj.ciudad.nombre

admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Comuna, ComunaAdmin)
