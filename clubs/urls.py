from django.contrib import admin
from django.urls import path
from clubs.views.ClubView import ClubView, GetClubDetailsView

urlpatterns = [
    path('makeTree/', ClubView.as_view()),
    path('getparents/', GetClubDetailsView.as_view()),
    
]