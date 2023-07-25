from django.urls import path
from . import views

urlpatterns = [
    path('', views.bodies_list, name='bodies_list'),
    path('events/', views.events_list, name='events_list')
    path('events/<int:pk>', views.event_detail, name='event_detail')
]