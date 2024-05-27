from django.urls import path

from graph.consumers import GraphConsumer

ws_urlpaterns = [
    path("ws/graph/", GraphConsumer.as_asgi()),
]
