from django.db import models
from product.models import Product


# Create your models here.
class Order(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=50, blank=False)
    contact_name = models.CharField(max_length=50, blank=False)
    address_1 = models.CharField(max_length=40, blank=False)
    address_2 = models.CharField(max_length=40, blank=False)
    address_3 = models.CharField(max_length=40, blank=True)
    address_4 = models.CharField(max_length=40, blank=True)
    post_code = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=40)
    landline_number = models.CharField(max_length=14, blank=True)
    mobile_number = models.CharField(max_length=14, blank=True)
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
