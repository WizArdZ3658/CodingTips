from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileListAPIView.as_view(), name='list')
]