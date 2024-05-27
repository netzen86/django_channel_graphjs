from django.urls import path

from graph.views import index


urlpatterns = [
    path("", index),
]
