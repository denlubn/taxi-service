# Generated by Django 4.1.1 on 2022-11-12 13:53

from django.db import migrations, models
import taxi.models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0004_car_image_alter_manufacturer_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="image",
            field=models.ImageField(
                blank=True, upload_to=taxi.models.car_image_file_path
            ),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="logo",
            field=models.ImageField(
                blank=True, upload_to=taxi.models.manufacturer_image_file_path
            ),
        ),
    ]
