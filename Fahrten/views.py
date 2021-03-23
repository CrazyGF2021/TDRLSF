
from Fahrten.models import Fahrten
from Absagen.models import Absagen
from users.models import CustomUser
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_date
from django.utils import timezone


def Fahrten_user(request):
    global fahrten
    global datum
    user = request.user.email
    if request.POST.get("datum") is None:
        datum = timezone.now().date()
        fahrten = Fahrten.objects.select_related('Schule__Kunde').prefetch_related('Schule__Nutzer').all().filter(
            Schule__Nutzer__email=user)

    elif request.POST.get("datum") is not None:
        datum = request.POST.get("datum")
        wtid = parse_date(datum).isoweekday()
        fahrten = Fahrten.objects.select_related('Schule__Kunde').prefetch_related('Schule__Nutzer').prefetch_related(
            'Wochentage').all().filter(Schule__Nutzer__email=user, gueltig_ab__lte=datum, gueltig_bis__gte=datum,
                                       Wochentage__wochentagID__exact=wtid,)

    context = ({'object_list': fahrten, 'Datum': datum})
    return render(request, 'Fahrten/Fahrtenlist_user.html', context)


def fahrten_detail(request, pk):
    fahrt = get_object_or_404(Fahrten, pk=pk)
    return render(request, 'Fahrten/fahrt_detail.html', {'Fahrten': fahrt})


def fahrten_Absage(request, pk):
    fahrt = get_object_or_404(Fahrten, pk=pk)
    datum = request.POST.get('datum')
    user = get_object_or_404(CustomUser, email=request.user.email)
    a = Absagen(Fahrt=fahrt,Datum=datum,user=user)
    a.save()
    return redirect('Fahrten_user')


