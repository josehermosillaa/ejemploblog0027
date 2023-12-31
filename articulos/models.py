from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Título')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'articulo'
        verbose_name_plural = 'articulos'
        ordering = ['-created']