# Generated by Django 5.0.2 on 2024-03-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps_google', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Short_Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(blank=True, max_length=200, null=True)),
                ('lng', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]