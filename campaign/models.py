from django.db.models import ForeignKey
from django.contrib.auth.models import User
from django.db import models
from enum import Enum
from organisation.models import Organisation
from round.models import Round


# Create your models here.
class CampaignChoice(Enum):
    LE = "Leafleting"
    CA = "Canvassing"
    SU = "Surveying"


class Campaign(models.Model):
    """
    This model links to one or more Rounds to create delivery routes for leafleting, canvassing,
    surveying, etc. A Campaign runs between a start and end date decided by the user. An end date
    can be left blank to denote an ongoing campaign with an indefinite end date.
    """
    objects = models.Manager()

    name = models.CharField(max_length=50)
    description = models.TextField()
    campaign_lead = models.CharField(max_length=50, blank=True)
    user = ForeignKey(User, null=True, on_delete=models.PROTECT)
    organisation = ForeignKey(Organisation, null=True, on_delete=models.PROTECT)
    campaign_type = models.CharField(max_length=15, choices=[(tag.name, tag.value)
                                                             for tag in CampaignChoice], default='LE')
    round = models.ForeignKey(Round, on_delete=models.PROTECT)
    active_date = models.DateField()
    inactive_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['active_date', 'campaign_type', 'name']

    def __str__(self):
        return 'Start date: {}, Campaign type: {}, Name: {}, Description: {}'.\
            format(self.active_date, self.campaign_type, self.name, self.description)


