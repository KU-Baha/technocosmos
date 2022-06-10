from django.contrib import admin
from config.models import SpaceObject, Status, Mission, Technology

# Register your models here.
admin.site.register(SpaceObject)
admin.site.register(Status)
admin.site.register(Mission)
admin.site.register(Technology)
