# Generated by Django 5.1.1 on 2024-10-28 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('idMenu', models.AutoField(primary_key=True, serialize=False)),
                ('namaMenu', models.CharField(default='', max_length=50)),
                ('hargaMenu', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deskripsiMenu', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Pemesanan',
            fields=[
                ('idPemesanan', models.AutoField(primary_key=True, serialize=False)),
                ('tanggalPemesanan', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Pemesanan',
            },
        ),
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('idPengunjung', models.AutoField(primary_key=True, serialize=False)),
                ('namaPengunjung', models.CharField(default='', max_length=50)),
                ('jenisKelamin', models.CharField(blank=True, max_length=10, null=True)),
                ('pekerjaan', models.CharField(blank=True, max_length=50, null=True)),
                ('alamat', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pengunjung',
            },
        ),
        migrations.CreateModel(
            name='Restoran',
            fields=[
                ('idRestoran', models.AutoField(primary_key=True, serialize=False)),
                ('namaRestoran', models.CharField(default='', max_length=50)),
                ('alamat', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Restoran',
            },
        ),
        migrations.CreateModel(
            name='DetailPemesananMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('totalHarga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idMenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pemesanan.menu')),
                ('idPemesanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pemesanan.pemesanan')),
            ],
            options={
                'verbose_name_plural': 'Detail Pemesanan Menu',
            },
        ),
        migrations.AddField(
            model_name='pemesanan',
            name='idPengunjung',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pemesanan.pengunjung'),
        ),
        migrations.AddField(
            model_name='pengunjung',
            name='idRestoran',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pemesanan.restoran'),
        ),
        migrations.AddField(
            model_name='menu',
            name='idRestoran',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pemesanan.restoran'),
        ),
    ]