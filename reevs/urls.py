from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("rest/", views.rests_list, name="rests"),
    path("booking/", views.book_rest, name="booking"),
    path("sef/", views.sef, name="sef"),
    path("bt/", views.bt, name="bt"),
]