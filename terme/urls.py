from django.urls import path
from django_todo.views import HelloWorld

urlpatterns = [
    path('', HelloWorld.as_view(), name="hello"),
]
