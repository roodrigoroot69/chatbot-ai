from django.urls import path
from src.chatlai.views import ChatBotWebHookAPIView


urlpatterns = [
    path('webhook/', ChatBotWebHookAPIView.as_view(), name='webhook'),
]
