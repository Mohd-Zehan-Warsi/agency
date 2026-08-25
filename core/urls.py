from django.urls import path
from .views import home , technology_detail

urlpatterns = [
    path("", home, name="home"),
    path("technologies/<slug:slug>/",technology_detail,name="technology_detail",),
]