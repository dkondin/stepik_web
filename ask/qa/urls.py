from django.conf.urls import include, url
from django.contrib import admin

from qa.views import test

urlpatterns = [
    url(r"^$", include("test")),
    url(r"^login/.*$", include("test")),
    url(r"^signup/.*", include("test")),
    url(r"^question/\d+/$", include("test")),
    url(r"^ask/.*", include("test")),
    url(r"^popular/.*", include("test")),
    url(r"^new/.*", include("test")),
]
