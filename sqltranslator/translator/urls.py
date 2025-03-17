from django.urls import path
from .views import translate, index


urlpatterns = [
    path("", index, name="index"),
    path("translate/", translate, name="translate"),
]