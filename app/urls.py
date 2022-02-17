from django.urls import path

from .views import button, index
urlpatterns = [
    path('', index),
    path('result/', button), 

]