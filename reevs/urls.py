from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("rest/", views.rooms_list, name="rests"),
    path("booking/", views.book_room, name="booking"),
]