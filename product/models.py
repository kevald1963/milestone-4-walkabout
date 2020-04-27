from django.db import models


# Create your models here.
class Product(models.Model):
    """
    NOTES:
    If a product is marked as a single use product then it means that it can only be combined with a
    non-single use product. Two or more subscriptions cannot be combined as it would be difficult to
    keep track of the number of users of each.
    """
    objects = models.Manager()

    number = models.SmallIntegerField(unique=True)
    name = models.CharField(max_length=254, default='')
    is_single_use_only = models.BooleanField(verbose_name='Is a single use product?', default=False)
    is_base_product = models.BooleanField(verbose_name='Is a base product?', default=False)
    is_upgrade_product = models.BooleanField(verbose_name='Is an upgrade product?', default=False)
    is_data_product = models.BooleanField(verbose_name='Is a data product?', default=False)
    max_product_quantity = models.SmallIntegerField(default=0)
    number_of_users = models.SmallIntegerField(default=0)
    number_of_subscription_months = models.SmallIntegerField(default=0)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_path = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    image_caption = models.CharField(max_length=70, blank=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return 'Product number: #{}, Description: {}'.format(self.number, self.name)


class Discount(models.Model):
    """
    Discounts for multiple product purchases and sales promotions.
    """
    objects = models.Manager()

    code = models.SmallIntegerField(unique=True)
    type = models.CharField(max_length=40, default='')
    percent = models.DecimalField(max_digits=5, decimal_places=1, blank=False)

    class Meta:
        ordering = ['code', 'type']

    def __str__(self):
        return 'Discount code: #{}, Discount type: {}, Discount percentage: {}%'.\
            format(self.code, self.type, self.percent)
