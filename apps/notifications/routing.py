from django.urls import path, re_path
from . import consumers

websocket_urlpatterns = [
    path('ws/users/', consumers.NotificationConsumer.as_asgi()),
]