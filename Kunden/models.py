from django.db import models

# Create your models here.
class Kunden(models.Model):
    Name = models.CharField(max_length=250)
    Strasse = models.CharField(max_length=50)
    Hausnummer = models.IntegerField()
    Postleitzahl = models.IntegerField()
    Stadt = models.CharField(max_length=50)
    email = models.EmailField('Email Addresse')

    class Meta:
        verbose_name = "Kunde"
        verbose_name_plural = "Kunden"

    def __str__(self):
        return self.Name


# Create your models here.
