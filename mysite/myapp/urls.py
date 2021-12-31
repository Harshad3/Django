from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:id>', views.book_id, name='book_id'),
    path('book', views.book_id2, name='book_id2'),

]