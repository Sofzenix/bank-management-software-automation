"""
Module: Authentication Routes
Source: Django users/urls.py
Purpose: URL mappings for auth APIs
"""
from django.urls import path
from .views import AdminOnlyTestView
from .views import AdminOnlyTestView, LoginAPIView

urlpatterns = [
    path('admin-test/', AdminOnlyTestView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('admin-test/', AdminOnlyTestView.as_view()),
]


