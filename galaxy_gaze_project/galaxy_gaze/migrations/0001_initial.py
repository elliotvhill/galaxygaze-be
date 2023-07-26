# Generated by Django 4.2.3 on 2023-07-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CelestialBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('distanceFromEarth', models.BigIntegerField(blank=True)),
                ('horizontal_pos', models.CharField(blank=True)),
                ('horizon_pos', models.CharField(blank=True)),
                ('equatorial_pos', models.CharField(blank=True)),
                ('extra_info', models.CharField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CosmicEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField()),
                ('event_date', models.CharField()),
                ('event_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField()),
                ('email', models.CharField()),
                ('password', models.CharField()),
            ],
        ),
    ]
