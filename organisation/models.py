from django.contrib.auth.models import User
from django.db import models
from product.models import Product


# Create your models here.
class Organisation(models.Model):
    objects = models.Manager()
    
    name = models.CharField(max_length=50, verbose_name='Enter name of your organisation or full name if not an '
                                                        'organisation.')
    description = models.TextField()
    contact_name = models.CharField(max_length=50, blank=True)
    is_parent = models.BooleanField(verbose_name='Is parent organisation?', default=False)
    logo_text = models.CharField(max_length=15, blank=True)
    glyphicon_name = models.CharField(max_length=20, blank=True)
    image_path = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    image_caption = models.CharField(max_length=70, blank=True)
    address_1 = models.CharField(max_length=40, blank=False)
    address_2 = models.CharField(max_length=40, blank=False)
    address_3 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    post_code = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=40)
    landline_number = models.CharField(max_length=14, blank=True)
    mobile_number = models.CharField(max_length=14, blank=True)
    # updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    objects = models.Manager()

    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    subscription_count = models.SmallIntegerField()

    class Meta:
        ordering = ['organisation', 'product']

    def __str__(self):
        return 'Organisation: {}, Product number: #{}'.format(self.organisation, self.product)
