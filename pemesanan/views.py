from django.shortcuts import render
from .models import Pemesanan, DetailPemesananMenu, Pengunjung
from django.db.models import Count, Sum

# Fungsi untuk halaman utama
def index(request):
    return render(request, 'laporan/index.html')  # Menampilkan laporan/index.html

# Fungsi untuk menampilkan menu terfavorit
def menu_terfavorit(request):
    menu_terfavorit = (
        DetailPemesananMenu.objects
        .values('idMenu__namaMenu')
        .annotate(total_pesanan=Sum('jumlahPesanan'))
        .order_by('-total_pesanan')
        .first()
    )
    return render(request, 'laporan/menu_terfavorit.html', {'menu_terfavorit': menu_terfavorit})

# Fungsi untuk menampilkan jumlah pengunjung per hari
def pengunjung_per_hari(request):
    pengunjung_per_hari = (
        Pemesanan.objects
        .values('tanggalPemesanan')
        .annotate(total_pengunjung=Count('idPengunjung', distinct=True))
        .order_by('tanggalPemesanan')
    )
    for data in pengunjung_per_hari:
        print(f"Tanggal: {data['tanggalPemesanan']}, Total Pengunjung: {data['total_pengunjung']}")
    return render(request, 'laporan/pengunjung_per_hari.html', {'pengunjung_per_hari': pengunjung_per_hari})

# Fungsi untuk menampilkan jumlah pemesanan per hari
def pemesanan_per_hari(request):
    pemesanan_per_hari = (
        Pemesanan.objects
        .values('tanggalPemesanan')
        .annotate(total_pemesanan=Count('idPemesanan'))
        .order_by('tanggalPemesanan')
    )
    return render(request, 'laporan/pemesanan_per_hari.html', {'pemesanan_per_hari': pemesanan_per_hari})

# Fungsi untuk menampilkan profesi terpopuler
def profesi_terpopuler(request):
    profesi_terpopuler = (
        Pengunjung.objects
        .values('pekerjaan')
        .annotate(total_kunjungan=Count('idPengunjung'))
        .order_by('-total_kunjungan')
    )
    return render(request, 'laporan/profesi_terpopuler.html', {'profesi_terpopuler': profesi_terpopuler})

# Fungsi untuk menampilkan pendapatan per hari
def pendapatan_per_hari(request):
    pendapatan_per_hari = (
        DetailPemesananMenu.objects
        .values('idPemesanan__tanggalPemesanan')
        .annotate(total_pendapatan=Sum('totalHarga'))
        .order_by('idPemesanan__tanggalPemesanan')
    )
    return render(request, 'laporan/pendapatan_per_hari.html', {'pendapatan_per_hari': pendapatan_per_hari})
