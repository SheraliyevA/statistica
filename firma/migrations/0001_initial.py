# Generated by Django 5.0.3 on 2024-03-04 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('xato_soni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Xodim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familiya', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='XodimMahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firma.mahsulot')),
                ('xodim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mahsulotlar', to='firma.xodim')),
            ],
        ),
    ]
