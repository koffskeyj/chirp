from django.shortcuts import render
from django.views.generic import ListView

from main.models import BirdSound

class IndexView(ListView):
    template_name = "index.html"
    model = BirdSound

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["amount"] = BirdSound.objects.all().count()
        return context
