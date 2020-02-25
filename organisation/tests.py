from django.test import TestCase
from .models import Organisation

# Create your tests here.
class OrganisationTests(TestCase):

    def test_org_name(self):
        test_organisation_name = Organisation(name = "South Tyneside Green Party")
        self.assertEqual(str(test_organisation_name), "South Tyneside Green Party")