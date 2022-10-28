from . import views
from django.urls import path

urlpatterns = [
    path('', views.FilmList.as_view(), name='home'),
    path('<slug:slug>/', views.FilmDetail.as_view(), name='film_detail'),
]