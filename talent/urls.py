# urls.py

from django.urls import path, include
from .views import UserProfileView, Testing, Test, TalentViewSet
from rest_framework import routers

rounter = routers.DefaultRouter()
rounter.register(r'api', TalentViewSet)


urlpatterns = [
    path('test/', Test.as_view(), name='test'),
    path('profile/', UserProfileView.as_view(), name='profiletesting'),
    path('api/', TalentViewSet.as_view({'get': 'list'}), name='api'),
    path('api/<int:pk>/', TalentViewSet.as_view({'get': 'retrieve'}), name='api'),  
     
]
