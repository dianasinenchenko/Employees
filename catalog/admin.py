from django.contrib import admin

# Register your models here.

from .models import Employees


#admin.site.register(Employees)


@admin.register(Employees)
class EmployessAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    fields = ['first_name', 'last_name', 'email']



