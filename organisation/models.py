from django.db import models

# Create your models here.
class Organisation(models.Model):

    objects = models.Manager()
    
    name = models.CharField(max_length = 50)
    description = models.TextField(300)
    logo_text = models.CharField(max_length = 15)
    glyphicon_name = models.CharField(max_length = 20)
    image_path = models.TextField(1024)
    image = models.ImageField(upload_to = 'images')
    address_1 = models.CharField(max_length = 30)
    address_2 = models.CharField(max_length = 30)
    address_3 = models.CharField(max_length = 30)
    address_4 = models.CharField(max_length = 30)
    post_code = models.CharField(max_length = 8)
    email_address = models.CharField(max_length = 40)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.name