from rest_framework.test import APITestCase
from rest_framework import status
from .tasks import read_bdm, read_dof, read_fixer
from .models import BdmExch, DofExch, FixerExch
from rest_framework_api_key.models import APIKey
import datetime

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

class KeyRetrievalTestCase(APITestCase):
    def test_key_retrieval(self):
        response = self.client.get("/api/v1/createkey/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Api-Key" in response.data)

class ServiceRetrievalWithErrorTestCase(APITestCase):
    def setUp(self):
        BdmExch.objects.create(time= datetime.datetime(2021, 3, 16, 1, 53, 54, 108659),exch=20.2222)
        DofExch.objects.create(time= datetime.datetime(2021, 3, 16, 1, 53, 54, 108659),exch=20.2222)
        FixerExch.objects.create(time= datetime.datetime(2021, 3, 16, 1, 53, 54, 108659),exch=20.2222)

    def test_fixer_reading(self):
        response = self.client.get("/api/v1/exchange/")
        self.assertEqual(response.status_code, 403)

class ServiceRetrievalTestCase(APITestCase):
    def setUp(self):
        BdmExch.objects.create(time= datetime.datetime(2021, 3, 16, 1, 53, 54, 108659),exch=20.2222)
        DofExch.objects.create(time= datetime.datetime(2021, 3, 16, 1, 53, 54, 108659),exch=20.2222)
        FixerExch.objects.create(time= datetime.datetime(2021, 3, 16, 1, 53, 54, 108659),exch=20.2222)
        keyres = self.client.get("/api/v1/createkey/")
        self.apikey = "Api-Key " + keyres.data["Api-Key"]

    def test_fixer_reading(self):
        response = self.client.get("/api/v1/exchange/", HTTP_AUTHORIZATION=self.apikey)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["Banco_de_Mexico"]["last_updated"],\
             '2021-03-16T01:53:54.108659-06:00')
        self.assertEqual(response.data["Banco_de_Mexico"]["value"], '20.2222')
        self.assertEqual(response.data["Diario_Oficial_de_la_Federacion"]["last_updated"],\
             '2021-03-16T01:53:54.108659-06:00')
        self.assertEqual(response.data["Diario_Oficial_de_la_Federacion"]["value"], '20.2222')        
        self.assertEqual(response.data["Fixer"]["last_updated"],\
             '2021-03-16T01:53:54.108659-06:00')
        self.assertEqual(response.data["Fixer"]["value"], '20.2222')

class KeyRetrievalTestCase(APITestCase):
    def test_key_retrieval(self):
        response = self.client.get("/api/v1/createkey/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Api-Key" in response.data)

class ThrottlingTestCase(APITestCase):
    def setUp(self):
        BdmExch.objects.create(time= datetime.datetime(2021, 3, 16, 1, 53, 54, 108659),exch=20.2222)
        DofExch.objects.create(time= datetime.datetime(2021, 3, 16, 1, 53, 54, 108659),exch=20.2222)
        FixerExch.objects.create(time= datetime.datetime(2021, 3, 16, 1, 53, 54, 108659),exch=20.2222)
        keyres = self.client.get("/api/v1/createkey/")
        self.apikey = "Api-Key " + keyres.data["Api-Key"]

    def test_fixer_reading(self):
        self.client.get("/api/v1/exchange/", HTTP_AUTHORIZATION=self.apikey)
        self.client.get("/api/v1/exchange/", HTTP_AUTHORIZATION=self.apikey)
        self.client.get("/api/v1/exchange/", HTTP_AUTHORIZATION=self.apikey)
        self.client.get("/api/v1/exchange/", HTTP_AUTHORIZATION=self.apikey)
        self.client.get("/api/v1/exchange/", HTTP_AUTHORIZATION=self.apikey)
        response = self.client.get("/api/v1/exchange/", HTTP_AUTHORIZATION=self.apikey)
        self.assertEqual(response.status_code, 429)

