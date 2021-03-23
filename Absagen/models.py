from django.db import models
from django.utils.timezone import now


class Absagen(models.Model):
     Fahrt = models.ForeignKey("Fahrten.Fahrten", on_delete=models.CASCADE)
     Datum = models.DateField()
     Absagezeitpunkt = models.DateTimeField(auto_now_add=True)
     date_created = models.DateTimeField('date created', default=now)
     date_updated = models.DateTimeField('date updated',default=now)
     user = models.ForeignKey("users.CustomUser", blank=True, on_delete=models.CASCADE)

     class Meta:
         verbose_name = "Absage"
         verbose_name_plural = "Absagen"

     #def Absage(self):
     #    self.Absagezeitpunkt = now()
     #    self.save()

     def save(self, *args, **kwargs):
         if not self.id:
             self.date_created = now()
         self.date_updated = now()
         super(Absagen, self).save(*args, **kwargs)

     def __int__(self):
         return self.Datum