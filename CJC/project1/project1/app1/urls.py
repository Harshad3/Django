from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('v2/', views.view2),
    path('v3/', views.view3),
]