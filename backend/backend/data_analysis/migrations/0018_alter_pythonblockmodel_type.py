# Generated by Django 4.2.6 on 2023-11-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_analysis", "0017_rename_text_pythonblockmodel_header_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pythonblockmodel",
            name="type",
            field=models.CharField(
                choices=[
                    ("python", "Python"),
                    ("sql", "SQL"),
                    ("metric", "Metric"),
                    ("chart", "Chart"),
                    ("table", "Table"),
                    ("heading1", "Heading1"),
                    ("heading2", "Heading2"),
                    ("heading3", "Heading3"),
                    ("Paragraph", "Paragraph"),
                ],
                default="python",
                max_length=255,
            ),
        ),
    ]
