from django.contrib import admin
from .models import inoutiProjects, clientesImg


# Register your models here.

class projectsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(inoutiProjects, projectsAdmin)

class clientsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(clientesImg, clientsAdmin)
