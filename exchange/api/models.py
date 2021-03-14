from django.db import models

class BdmEpixch(models.Model):
    id = models.AutoField(primary_key=True)
    exch = models.DecimalField(decimal_places=14)
    time = models.DateTimeField()

class DofExch(models.Model):
    id = models.AutoField(primary_key=True)
    exch = models.DecimalField(decimal_places=14)
    time = models.DateTimeField()

class FixerExch(models.Model):
    id = models.AutoField(primary_key=True)
    exch = models.DecimalField(decimal_places=14)
    time = models.DateTimeField()