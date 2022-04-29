from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home),
    path('production/', views.production),
    path('attestation/', views.attestation),
]

