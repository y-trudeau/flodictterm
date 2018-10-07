from django.conf.urls.defaults import *
from . import views

urlpatterns = [
    path('', HelloWorld.as_view(), name="hello"),
]
