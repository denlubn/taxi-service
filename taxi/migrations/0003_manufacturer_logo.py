# Generated by Django 4.1.1 on 2022-10-05 16:20

from django.db import migrations, models
import taxi.models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_car_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="manufacturer",
            name="logo",
            field=models.ImageField(
                null=True, upload_to=taxi.models.manufacturer_image_file_path
            ),
        ),
    ]