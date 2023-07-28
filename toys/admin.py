from django.contrib import admin
from .models import Toys

# Register your models here.
class ToysAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'date', 'freq']

admin.site.register(Toys, ToysAdmin)