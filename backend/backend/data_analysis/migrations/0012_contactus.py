# Generated by Django 4.2.6 on 2023-11-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_analysis", "0011_pythonblockmodel_python_code"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                ("contactusId", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.CharField(max_length=255)),
                ("fullname", models.CharField(max_length=255)),
                ("message", models.TextField(null=True)),
            ],
        ),
    ]
