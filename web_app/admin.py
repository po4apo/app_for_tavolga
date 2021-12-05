from django.contrib import admin
from .models import CustomUser, Event, Nomination, Document

admin.site.register(CustomUser)
admin.site.register(Event)
admin.site.register(Nomination)
admin.site.register(Document)
