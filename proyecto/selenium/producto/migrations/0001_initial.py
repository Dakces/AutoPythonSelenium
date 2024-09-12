# Generated by Django 5.1.1 on 2024-09-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
    ]
