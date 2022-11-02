from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date_purchase = models.DateField('дата покупки')

    def __str__(self):
        return f'{self.item.name} - {self.item}'


