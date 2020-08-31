from clubs.views.ClubPaymentView import GrandParentPaymentView, ParentPaymentView
from django.contrib import admin
from django.urls import path
from clubs.views.ClubView import ClubView, GetClubDetailsView

urlpatterns = [
    path('makeTree/', ClubView.as_view()),
    path('getparents/', GetClubDetailsView.as_view()),
    path('uploadgrandparentss/', GrandParentPaymentView.as_view()),
    path('uploadparentss/', ParentPaymentView.as_view()),
    
]