from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Games(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='Games')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
