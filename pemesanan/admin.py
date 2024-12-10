from django.contrib import admin
from .models import Restoran, Pengunjung, Menu, Pemesanan, DetailPemesananMenu

class DetailPemesananMenuAdmin(admin.ModelAdmin):
    readonly_fields = ('totalHarga',)  # Jadikan totalHarga read-only
    list_display = ('id', 'idPemesanan', 'idMenu', 'jumlahPesanan', 'totalHarga')  # Menampilkan kolom ini di list view
    list_filter = ('idPemesanan__tanggalPemesanan', 'idMenu__namaMenu')  # Memungkinkan filter berdasarkan tanggal pemesanan dan menu
    search_fields = ('idPemesanan__id', 'idMenu__namaMenu')  # Memungkinkan pencarian berdasarkan ID Pemesanan atau nama Menu

admin.site.register(Restoran)
admin.site.register(Pengunjung)
admin.site.register(Menu)
admin.site.register(Pemesanan)
admin.site.register(DetailPemesananMenu, DetailPemesananMenuAdmin)
