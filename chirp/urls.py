"""chirp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from main.views import IndexView, BirdSoundDetailView, CreateBirdSoundView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^bird_sound/(?P<pk>\d+)/$', BirdSoundDetailView.as_view(), name="bird_sound_detail_view"),
    url(r'^create_bird_sound/$', CreateBirdSoundView.as_view(), name="create_bird_sound_view")

]
