"""
    URL configuration for static pages
    @package networktechsolutions
    @author Noel Nagy
    @website: https://github.com/nagynooel
    ©2023 Noel Nagy - All rights reserved.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="index")
]