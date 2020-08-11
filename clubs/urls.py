from django.contrib import admin
from django.urls import path
from clubs.views.ClubView import ClubView

urlpatterns = [
    path('makeTree/', ClubView.as_view()),
    
]