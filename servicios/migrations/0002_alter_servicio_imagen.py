# Generated by Django 4.2.13 on 2024-05-29 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='servicios'),
        ),
    ]
