from django.contrib.auth.models import User
from django.db import models
from enum import Enum
from organisation.models import Organisation
from round.models import Round


# Create your models here.
class CampaignChoice(Enum):
    """
    Enumerate list for campaign type in Campaign model.
    """
    LEAFLET = "Leafleting"
    CANVASS = "Canvassing"
    SURVEY = "Surveying"


class Campaign(models.Model):
    """
    A Campaign links to one or more Rounds to create delivery routes for leafleting, canvassing,
    surveying, etc. A Campaign runs between a start and end date decided by the user. An end date
    can be left blank to denote an ongoing campaign with an indefinite end date.
    """
    objects = models.Manager()

    name = models.CharField(max_length=40)
    description = models.TextField()
    campaign_lead = models.CharField(max_length=50, blank=True)
    organisation = models.ForeignKey(Organisation, null=True, on_delete=models.PROTECT)
    campaign_type = models.CharField(max_length=20, choices=[(tag.name, tag.value)
                                                             for tag in CampaignChoice], default='LEAFLET')
    rounds = models.ManyToManyField(Round, blank=True)
    assigned_users = models.ManyToManyField(User, blank=True)
    active_date = models.DateField()
    inactive_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['name', 'active_date','campaign_type', ]

    def __str__(self):
        return 'Name: {}, Start date: {}, Description: {}, Type: {}'.\
            format(self.name, self.active_date, self.description, self.campaign_type)
