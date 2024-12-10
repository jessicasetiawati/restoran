from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-terfavorit/', views.menu_terfavorit, name='menu_terfavorit'),
    path('pengunjung-per-hari/', views.pengunjung_per_hari, name='pengunjung_per_hari'),
    path('pemesanan-per-hari/', views.pemesanan_per_hari, name='pemesanan_per_hari'),
    path('profesi-terpopuler/', views.profesi_terpopuler, name='profesi_terpopuler'),
    path('pendapatan-per-hari/', views.pendapatan_per_hari, name='pendapatan_per_hari'),
]
from django.shortcuts import render

def index(request):
    return render(request, 'laporan/index.html')  # Arahkan ke index.html di pemesanan/templates/laporan
