from django.db import models

class fahrten(models.QuerySet):
    def MoIsTrue(self):
        return self.filter(Mo=True)

    def DiIsTrue(self):
        return self.filter(Di=True)

    def MiIsTrue(self):
        return self.filter(Mi=True)

    def DoIsTrue(self):
        return self.filter(Do=True)

    def FrIsTrue(self):
        return self.filter(Fr=True)

class fahrten_Manager(models.Manager):
    def get_queryset(self):
        return fahrten(self.model, using=self._db)

    def MoisTrue(self):
        return self.get_queryset().MoIsTrue()

    def DiisTrue(self):
        return self.get_queryset().DiIsTrue()

    def MiisTrue(self):
        return self.get_queryset().MiIsTrue()

    def DoisTrue(self):
        return self.get_queryset().DoIsTrue()

    def FrisTrue(self):
        return self.get_queryset().FrIsTrue()
