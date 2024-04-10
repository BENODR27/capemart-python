from django.urls import path
from .controllers import apiController


urlpatterns= [
    path('test',apiController.home),
]
