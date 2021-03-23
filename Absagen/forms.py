import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django import forms

from .models import Absagen

class AbsagenForm(forms.ModelForm):

    class Meta:
         model = Absagen
         fields = ('title', 'text',)