# Generated by Django 4.2.6 on 2023-10-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_analysis", "0007_dataurlmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataurlmodel",
            name="path",
            field=models.FileField(blank=True, null=True, upload_to="dataurl", verbose_name="upload Field"),
        ),
    ]
