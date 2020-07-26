from django.urls import path
from . import views

urlpatterns = [
    path("<str:birthday>", views.index, name="index")
]