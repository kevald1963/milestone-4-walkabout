from django.db import models


# Create your models here.
class Product(models.Model):
    objects = models.Manager()

    number = models.SmallIntegerField()
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return 'Product number: #{}, Description: {}'.format(self.number, self.name)
