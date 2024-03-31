from django.contrib import admin
from testapp.models import Bikes
# Register your models here.

class BikeAdmin(admin.ModelAdmin):
    list_display=['id','name','engine','milage','price']
admin.site.register(Bikes,BikeAdmin)