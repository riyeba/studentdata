# Generated by Django 4.1.13 on 2023-11-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsuapp', '0003_alter_info_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='image',
            field=models.ImageField(max_length=255, upload_to='image/'),
        ),
    ]
