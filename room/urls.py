from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('roomdata', views.view_rooms),
    path('<int:id>', views.view_rooms_by_id),
]
