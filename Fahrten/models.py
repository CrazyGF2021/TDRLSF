from django.db import models
from djmoney.models.fields import MoneyField
from .managers import fahrten_Manager


class Fahrten(models.Model):
    Bezeichnung = models.CharField(max_length=250)
    Von = models.CharField(max_length=50)
    Nach = models.CharField(max_length=50)
    Abfahrt = models.TimeField()
    Ankunft = models.TimeField()
    Mo = models.BooleanField()
    Di = models.BooleanField()
    Mi = models.BooleanField()
    Do = models.BooleanField()
    Fr = models.BooleanField()
    Wochentage = models.ManyToManyField("Fahrten.Wochentag",  blank=True)
    zweiteWoche = models.BooleanField()
    Startdatum = models.DateField()
    gueltig_ab = models.DateField()
    gueltig_bis = models.DateField()
    Kuschikbezeichnung = models.CharField(max_length=255, blank=False)
    Schule = models.ForeignKey("Schule.Schule", on_delete=models.CASCADE, blank=False)
    Preis = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='EUR')

    class Meta:
        verbose_name = "Fahrt"
        verbose_name_plural = "Fahrten"

    def __str__(self):
        return self.Bezeichnung

    objects = models.Manager()
    fahrten = fahrten_Manager()

class Wochentag(models.Model):
    wochentag = models.CharField(max_length=20, unique=True, null=True)
    wochentagID = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Wochentag"
        verbose_name_plural = "Wochentage"

    def __str__(self):
        return self.wochentag