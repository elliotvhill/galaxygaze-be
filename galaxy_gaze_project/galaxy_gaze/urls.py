from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('bodies/', views.BodiesList.as_view(), name='bodies_list'),
    path('bodies/<int:id>', views.BodyDetail.as_view(), name="body_detail"),
    path('events/', views.EventsList.as_view(), name='events_list'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
    path('users/', views.UsersList.as_view(), name='users_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('deepspaceobject/', views.DeepSpaceObjectList.as_view(), name='deep_space_list'),
    path('deepspaceobject/search/', views.deepspaceobject_view, name='deepspaceobject-search'),
    path('api/get_user_id', views.get_user_id, name='get_user_id')
]