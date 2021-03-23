from Fahrten.models import Fahrten
from Absagen.models import Absagen
from users.models import CustomUser
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_date
from django.utils import timezone


def Absagen_user(request):
    global absagen
    global datum
    user = request.user.email
    datum = timezone.now().date()
    absagen = Absagen.objects.all()

    context = ({'object_list': absagen, 'Datum': datum})
    return render(request, 'Absagen/Absagen.html', context)
