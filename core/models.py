from django.db import models
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=8)
    image = models.ImageField(blank=False, null=False)
    id_athletic = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['name']

    def __str__(self):
        return self.name
