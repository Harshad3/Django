from django.urls import path
from .views import studentview


urlpatterns = [
    path('sv/', studentview)
]