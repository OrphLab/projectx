from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from . import serializers
from .models import Talent


class TalentViewSet(viewsets.ModelViewSet):
    queryset = Talent.objects.all()
    serializer_class = serializers.TalentSerializer
    
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)



@method_decorator(login_required, name='dispatch')


class UserProfileView(TemplateView):
    template_name = 'profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_data'] = self.request.user
        return context


class Testing(TemplateView):
    template_name = 'profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_data'] = self.request.user
        return context

class Test(TemplateView):
    template_name = 'test.html'
    

