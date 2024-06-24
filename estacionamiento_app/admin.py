from django.contrib import admin
from .models import Categoria, Escalafon, Dependencia, Usuario
admin.site.register(Categoria)
admin.site.register(Escalafon)
admin.site.register(Dependencia)
admin.site.register(Usuario)

# Register your models here.
