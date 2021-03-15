from rest_framework.test import APITestCase
from .tasks import read_bdm, read_dof, read_fixer
from .models import BdmExch, DofExch, FixerExch

class BDMParsingTestCase(APITestCase):
    def test_bdm_reading(self):
        read_bdm()
        self.assertTrue(BdmExch.objects.latest('id'))

class DOFParsingTestCase(APITestCase):
    def test_dof_reading(self):
        read_dof()
        self.assertTrue(DofExch.objects.latest('id'))

class FixerParsingTestCase(APITestCase):
    def test_fixer_reading(self):
        read_fixer()
        self.assertTrue(FixerExch.objects.latest('id'))
        
