from django.db import models

# Create your models here.

class Categoria (models.Model):
    nombre_categoria = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre_categoria

class Producto (models.Model):
    nombre_producto = models.CharField(max_length=200)
    precio_producto = models.FloatField()
    categoria_producto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen_producto = models.ImageField(upload_to="tienda", null=True, blank=True)
    disponibilidad_producto = models.BooleanField(default=True)
  

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre_producto
    

