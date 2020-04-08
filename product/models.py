from django.db import models


# Create your models here.
class Product(models.Model):
    objects = models.Manager()

    number = models.SmallIntegerField()
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_path = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    image_caption = models.CharField(max_length=70, blank=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return 'Product number: #{}, Description: {}'.format(self.number, self.name)
