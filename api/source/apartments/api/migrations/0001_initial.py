# Generated by Django 5.0.2 on 2024-02-23 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('floor', models.PositiveIntegerField()),
                ('building', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=32)),
                ('area_m2', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('description', models.TextField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
