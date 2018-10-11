from django.conf.urls import *
from terme.views import HelloWorld

urlpatterns = [
    url('', HelloWorld.as_view(), name="hello"),
]
