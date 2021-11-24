from django.contrib import admin
from . import models


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome')
    list_display_links = ('id', 'nome', 'sobrenome')
    #list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ("nome", 'sobrenome')

admin.site.register(models.Categoria)
admin.site.register(models.Contato, ContatoAdmin)
