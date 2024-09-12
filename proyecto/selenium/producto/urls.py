from django.urls import path
from . import views

urlpatterns = [
    path("mostrar/", views.index, name="index"),
]
