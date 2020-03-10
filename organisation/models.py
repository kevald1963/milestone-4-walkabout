from django.db import models

# Create your models here.
class Organisation(models.Model):

    objects = models.Manager()
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_parent = models.BooleanField(verbose_name='Is parent organisation?', default=False)
    logo_text = models.CharField(max_length=15, blank=True)
    glyphicon_name = models.CharField(max_length=20, blank=True)
    image_path = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    image_caption = models.CharField(max_length=70, blank=True)
    address_1 = models.CharField(max_length=40)
    address_2 = models.CharField(max_length=40)
    address_3 = models.CharField(max_length=40, blank=True)
    address_4 = models.CharField(max_length=40, blank=True)
    post_code = models.CharField(max_length=10)
    email_address = models.CharField(max_length=40)

    def __str__(self):
        return self.name
