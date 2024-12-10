# Generated by Django 5.1.1 on 2024-11-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemesanan', '0009_alter_detailpemesananmenu_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailpemesananmenu',
            name='jumlahPesanan',
            field=models.IntegerField(default=1, verbose_name='Jumlah pesanan'),
        ),
        migrations.AlterField(
            model_name='detailpemesananmenu',
            name='totalHarga',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Total harga'),
        ),
    ]