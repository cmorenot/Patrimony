from django.contrib import admin
from .models import Resource, FixingActions, Imagen, Threats, GeoLocalization, Area
# Register your models here.

admin.site.register(Resource)
admin.site.register(FixingActions)
admin.site.register(Imagen)
admin.site.register(Threats)
admin.site.register(GeoLocalization)
admin.site.register(Area)


