from django.db import models

# Create your models here.

class inoutiProjects(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    url = models.URLField(verbose_name='URL')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

class clientesImg(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    image = models.ImageField(verbose_name='Imagen', upload_to='clients')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'