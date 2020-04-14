from django.db import models


# Create your models here.
class Product(models.Model):
    """
    NOTES:
    If a product is marked as a subscription product then it means that it can only be combined with a
    non-subcription product. Two or more subscriptions cannot be combined as it would be difficult to
    keep track of the number of users of each.
    """
    objects = models.Manager()

    number = models.SmallIntegerField(unique=True)
    name = models.CharField(max_length=254, default='')
    is_subscription_product = models.BooleanField(verbose_name='Is a subscription product?', default=False)
    is_upgrade_product = models.BooleanField(verbose_name='Is an upgrade product?', default=False)
    is_data_product = models.BooleanField(verbose_name='Is a data product?', default=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_path = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    image_caption = models.CharField(max_length=70, blank=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return 'Product number: #{}, Description: {}'.format(self.number, self.name)
