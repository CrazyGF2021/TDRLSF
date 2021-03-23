from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Schule(models.Model):
    Name = models.CharField(max_length=250)
    Strasse = models.CharField(max_length=50)
    Hausnummer = models.IntegerField()
    Postleitzahl = models.IntegerField()
    Stadt = models.CharField(max_length=50)
    email = models.EmailField('Email Addresse')
    Kunde = models.ForeignKey("Kunden.Kunden", on_delete=models.CASCADE, blank=False)
    Nutzer = models.ManyToManyField("users.CustomUser", blank=True)

    class Meta:
        verbose_name = "Schule"
        verbose_name_plural = "Schulen"

    def __str__(self):
        return self.Name