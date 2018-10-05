from django.urls import path
from . import views

urlpatterns = [
    path('', HelloWorld.as_view(), name="hello"),
]
