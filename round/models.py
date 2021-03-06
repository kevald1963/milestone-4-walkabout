from django.db import models


# Create your models here.
class Round(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Street(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=30)
    comments = models.TextField(blank=True)
    door_number_start = models.SmallIntegerField()
    door_number_end = models.SmallIntegerField()
    round = models.ForeignKey(Round, on_delete=models.PROTECT, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=False, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Address(models.Model):
    objects = models.Manager()

    door_number = models.SmallIntegerField()
    name = models.ForeignKey(Street)
    comments = models.CharField(max_length=80, blank=True)

    class Meta:
        ordering = ['name', 'door_number']

    def __str__(self):
        return '{} {}'.format(self.door_number, self.name)
