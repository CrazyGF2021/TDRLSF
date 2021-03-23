import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Absagen
from Fahrten.models import Fahrten

class FahrtenInline(admin.StackedInline):
    model = Fahrten

class ExportCsvMixin:

    def __init__(self):
        self.model = None

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

# Register your models here.
@admin.register(Absagen)
class AbsagenAdmin(admin.ModelAdmin, ExportCsvMixin):
    date_hierarchy = 'Datum'
    actions = ["export_as_csv"]
    list_per_page = 50
    #def FahrtenName(self, obj):
    #    return ", ".join([
    #    Fahrten.Bezeichnung for  in obj.Fahrten.all()
    #                      ])
    #FahrtenName.short_description = "Fahrten"