from django.db import models


# Create your models here.
class Round(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name


class Street(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=40)
    comments = models.TextField(blank=True)
    door_number_start = models.SmallIntegerField()
    door_number_end = models.SmallIntegerField()
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    post_code = models.CharField(max_length=10, null=False, blank=True)

    def __str__(self):
        return self.name