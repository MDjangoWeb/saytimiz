# Generated by Django 3.1 on 2020-08-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jamoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('familya', models.CharField(max_length=50)),
                ('soha', models.CharField(max_length=50)),
                ('rasm', models.ImageField(upload_to='rasmlar/jamoa_rasm')),
                ('izox', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('familya', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', models.CharField(max_length=15)),
                ('rasm', models.ImageField(upload_to='rasmlar/profil_pic')),
            ],
        ),
    ]
