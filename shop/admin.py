from django.contrib import admin
from .models import itemShop

# Register your models here.

class itemAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(itemShop, itemAdmin)
