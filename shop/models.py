from django.db import models

# Create your models here.


class categoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class itemShop(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    img = models.ImageField(upload_to='shop', verbose_name='Imagen')
    description = models.TextField(verbose_name='Descripción')
    category = models.ManyToManyField(categoryModel, verbose_name='Categoria')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'