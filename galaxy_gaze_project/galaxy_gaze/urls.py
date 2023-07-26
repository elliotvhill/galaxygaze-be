from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('bodies/', views.BodiesList.as_view(), name='bodies_list'),
    path('bodies/<int:id>', views.BodyDetail.as_view(), name="body_detail"),
    path('events/', views.EventsList.as_view(), name='events_list'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
    # path('users/', views.users_list, name='users_list'),
    # path('users/<int:pk>', views.user_detail, name='user_detail'),
]