# Generated by Django 4.2.6 on 2023-10-30 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("data_analysis", "0008_dataurlmodel_path"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlockModel",
            fields=[
                ("blockId", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "workspace_id",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="data_analysis.workspace"),
                ),
            ],
        ),
    ]
