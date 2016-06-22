from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from main.models import StopWord, BirdSound, Profile

class IndexView(CreateView):
    template_name = "index.html"
    model = BirdSound
    fields = ["body"]
    success_url = reverse_lazy("index_view")

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = BirdSound.objects.all()
        context["amount"] = BirdSound.objects.all().count()
        return context


class BirdSoundDetailView(DetailView):
    model = BirdSound

    def get_queryset(self):
        return BirdSound.objects.filter(bird=self.request.user)


class ProfileUpdateView(UpdateView):
    fields = ["favorite_bird"]
    success_url = reverse_lazy("profile_update_view")

    def get_object(self, queryset=None):
        return self.request.user.profile


class BirdSoundDeleteView(DeleteView):
    success_url = reverse_lazy("index_view")

    def get_queryset(self):
        return BirdSound.objects.filter(bird=self.request.user)
