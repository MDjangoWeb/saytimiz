# Generated by Django 3.1 on 2020-08-29 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_jamoa_mijoz'),
    ]

    operations = [
        migrations.CreateModel(
            name='MijozFikr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fikr', models.TextField()),
                ('mijoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mijoz')),
            ],
        ),
    ]
