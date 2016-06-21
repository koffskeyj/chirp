from django.contrib import admin
from main.models import BirdSound

class BirdSoundAdmin(admin.ModelAdmin):
    list_display = ["body", "bird"]
    search_fields = ["body"]

admin.site.register(BirdSound, BirdSoundAdmin)
