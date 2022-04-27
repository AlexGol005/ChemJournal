from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('production/', views.production),
    path('attestation/', views.attestation),
    path('VG/', views.VG),
    path('K/', views.K),
]

