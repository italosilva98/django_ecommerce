from django.contrib import admin
from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView
urlpatterns = [
        path('', HomePageView.as_view(), name="homepage"),
        path('about/', AboutPageView.as_view(), name="about"),
        path('contact/', ContactPageView.as_view(), name="contact"),
]