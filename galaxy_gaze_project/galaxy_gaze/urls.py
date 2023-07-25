from django.urls import path
from . import views

urlpatterns = [
    path('', views.bodies_list, name='bodies_list'),
    path('', views.events_list, name='events_list'),
]