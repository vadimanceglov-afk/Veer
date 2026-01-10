from django.urls import path
from . import views

urlpatterns = [
    path("rest/", views.rooms_list, name="rests")
]