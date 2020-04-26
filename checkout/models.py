from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.models import User
from product.models import Product


# Create your models here.
class Order(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=50, blank=False, verbose_name='Name of your organisation or full '
                                                                     'name if not an organisation.')
    user = ForeignKey(User, null=True)
    address_1 = models.CharField(max_length=40, blank=False)
    address_2 = models.CharField(max_length=40, blank=False)
    address_3 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    post_code = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=40)
    mobile_number = models.CharField(max_length=14, blank=False)
    date = models.DateField(blank=True)

    def __str__(self):
        return "{}-{}".format(self.date, self.name)


class OrderLineItem(models.Model):
    objects = models.Manager()

    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)
