from django.conf.urls import *
from . import views

urlpatterns = [
    url('', HelloWorld.as_view(), name="hello"),
]
