from datetime import datetime
from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.IntegerField()
    price = models.FloatField()
    old_price = models.FloatField(default=0)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='products'
    )

    class Meta:
        ordering = ['-pk']
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты/ов'


class Card(models.Model):
    product = models.ForeignKey(
        Product,
        blank=True,
        null=2,
        on_delete=models.SET_NULL,
        related_name='card_products'
    )
    add_datetime = models.DateTimeField(default=datetime.now)
    count = models.IntegerField(default=1)

    class Meta:
        ordering = ['-pk']