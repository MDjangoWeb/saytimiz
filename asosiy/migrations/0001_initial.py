# Generated by Django 3.1 on 2020-08-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ish_nomi', models.CharField(max_length=100)),
                ('toifa', models.CharField(max_length=500)),
                ('rasm', models.ImageField(upload_to='rasmlar/portfolio_rasm')),
                ('izox', models.TextField()),
            ],
        ),
    ]