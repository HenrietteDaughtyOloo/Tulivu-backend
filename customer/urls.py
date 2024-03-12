from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

#URLConf model
urlpatterns = [
    path('welcome/', views.welcome_customer),
    path('customerdata', views.CustomerDataJsonFun),
    path('<int:id>', views.customer_by_id),  
]
urlpatterns = format_suffix_patterns(urlpatterns)