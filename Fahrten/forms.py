import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class Datumsauswahl(forms.Form):
    datum = forms.DateField(help_text="Bitte wählen Sie einen Fahrtag aus.")

    def clean_renewal_date(self):
        data = self.cleaned_data['Fahrtag']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Das ausgewählte Datum liegt in der Vergangenheit'))


        # Remember to always return the cleaned data.
        return data