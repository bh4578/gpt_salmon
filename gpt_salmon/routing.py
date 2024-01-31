from django.urls import path
from gpt_service import consumers

websocket_urlpatterns = [
    path('ws/gpt/', consumers.Myconsumers.as_asgi()),
]