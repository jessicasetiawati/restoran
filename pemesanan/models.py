from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Model Restoran
class Restoran(models.Model):
    idRestoran = models.AutoField(primary_key=True)
    namaRestoran = models.CharField(max_length=50, null=False,verbose_name='nama restoran', default="")
    alamat = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Restoran'

    def __str__(self):
        return self.namaRestoran

# Model Pengunjung
class Pengunjung(models.Model):
    pilihJK=[
        ('l','laki-laki'),('p','perempuan'),
    ]
    idPengunjung = models.AutoField(primary_key=True)
    idRestoran = models.ForeignKey(Restoran, on_delete=models.CASCADE)
    namaPengunjung = models.CharField(max_length=50,verbose_name='nama pengunjung', null=False, default="")
    jenisKelamin = models.CharField(max_length=11,verbose_name='jenis kelamin', null=True,choices=pilihJK)
    pekerjaan = models.CharField(max_length=50, null=True, blank=True)
    alamat = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Pengunjung'

    def __str__(self):
        return f"{self.namaPengunjung}"

# Model Menu
class Menu(models.Model):
    idMenu = models.AutoField(primary_key=True)
    idRestoran = models.ForeignKey(Restoran, on_delete=models.CASCADE)
    namaMenu = models.CharField(max_length=50, null=False,verbose_name='nama menu', default="")
    hargaMenu = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='harga Menu')  # Harga menu
    deskripsiMenu = models.TextField(null=True, blank=True,verbose_name='deskripsi menu')

    class Meta:
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.namaMenu

# Model Pemesanan
class Pemesanan(models.Model):
    idPemesanan = models.AutoField(primary_key=True)
    idPengunjung = models.ForeignKey(Pengunjung, on_delete=models.CASCADE)
    tanggalPemesanan = models.DateField(null=False,verbose_name='Tanggal Pemesanan')

   
    class Meta:
        verbose_name_plural = 'Pemesanan'

    def __str__(self):
        return f" {self.idPemesanan} oleh {self.idPengunjung.namaPengunjung}"

# Model DetailPemesananMenu
class DetailPemesananMenu(models.Model):
    id = models.AutoField(primary_key=True)
    idMenu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    idPemesanan = models.ForeignKey(Pemesanan, on_delete=models.CASCADE)
    jumlahPesanan = models.IntegerField(default=1,verbose_name='Jumlah pesanan')
    totalHarga = models.DecimalField(max_digits=10,verbose_name='Total harga', decimal_places=2, editable=False)

    class Meta:
        verbose_name_plural = 'detail pemesanan menu'

    def __str__(self):
        return f"  {self.idPemesanan} oleh {self.idMenu.namaMenu}"


    def save(self, *args, **kwargs):
        # Pastikan harga dihitung dengan benar
        self.totalHarga = self.jumlahPesanan * self.idMenu.hargaMenu
        super().save(*args, **kwargs)