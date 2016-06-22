from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from main.models import StopWord

from main.models import BirdSound

class IndexView(ListView):
    template_name = "index.html"
    model = BirdSound

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["amount"] = BirdSound.objects.all().count()
        return context


class BirdSoundDetailView(DetailView):
    model = BirdSound

    def get_queryset(self):
        return BirdSound.objects.filter(bird=self.request.user)


class CreateBirdSoundView(CreateView):
    model = BirdSound
    fields = ["body"]
    success_url = "/"

    def form_valid(self, form):
        stop_words = StopWord.objects.all()
        birdsound_body = form.cleaned_data["body"].lower()
        for stop_word in stop_words:
            if stop_word.word in birdsound_body:
                form.add_error("body", "Blah")
                return self.form_invalid(form)
        birdsound = form.save(commit=False)
        birdsound.bird = self.request.user
        return super().form_valid(form)
