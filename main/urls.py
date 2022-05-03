from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('production/', views.production),
    path('attestation/', views.attestation),
]

