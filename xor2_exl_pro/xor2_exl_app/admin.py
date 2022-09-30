from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Person

# Register your models here.
admin.site.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id','first_name','last_name','email','gender','ip_address')