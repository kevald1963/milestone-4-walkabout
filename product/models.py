from django.db import models


# Create your models here.
class Product(models.Model):
    """
    NOTES:
    If a product is marked as a unique product then it means that it can only be combined with a non-unique product.
    For example subcriptions are unique products. They cannot be combined as it would be difficult to keep track of
    a subscription for an organisation with two different sets of use licences.
    """
    objects = models.Manager()

    number = models.SmallIntegerField()
    name = models.CharField(max_length=254, default='')
    is_unique_product = models.BooleanField(verbose_name='Is a unique product?', default=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_path = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    image_caption = models.CharField(max_length=70, blank=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return 'Product number: #{}, Description: {}'.format(self.number, self.name)
