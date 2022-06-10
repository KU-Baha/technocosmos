from django.contrib import admin
from config.models import Planet, Status, Mission, Technology

# Register your models here.
admin.site.register(Planet)
admin.site.register(Status)
admin.site.register(Mission)
admin.site.register(Technology)