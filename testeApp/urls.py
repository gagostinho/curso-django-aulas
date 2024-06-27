from django.urls import path
from testeApp.views import home

urlpatterns = [
    path('', home),
]
