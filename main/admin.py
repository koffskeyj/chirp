from django.contrib import admin
from main.models import BirdSound, StopWord

class BirdSoundAdmin(admin.ModelAdmin):
    list_display = ["body", "bird"]
    search_fields = ["body"]

admin.site.register(BirdSound, BirdSoundAdmin)

class StopWordAdmin(admin.ModelAdmin):
    list_display = ["word"]
    search_fields = ["word"]

admin.site.register(StopWord, StopWordAdmin)
