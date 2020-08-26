from django.contrib import admin

# Register your models here.

from .models import Articolo,Giornalista

admin.site.register(Articolo)
admin.site.register(Giornalista)