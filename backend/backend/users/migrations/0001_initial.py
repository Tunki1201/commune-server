# Generated by Django 4.2.6 on 2023-10-09 23:52

import backend.users.managers
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("company_id", models.AutoField(primary_key=True, serialize=False)),
                ("company_email", models.EmailField(max_length=254, unique=True)),
                ("company_name", models.CharField(max_length=255)),
                ("company_logo", models.ImageField(blank=True, null=True, upload_to="company_logos/")),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                ("fullname", models.CharField(default="John Doe", max_length=255)),
                ("name", models.CharField(blank=True, max_length=255, verbose_name="Name of User")),
                ("email", models.EmailField(max_length=254, unique=True, verbose_name="email address")),
                (
                    "user_type",
                    models.CharField(
                        choices=[
                            ("Data Engineer", "Data Engineer"),
                            ("Data Analyst", "Data Analyst"),
                            ("Data Scientist", "Data Scientist"),
                            ("Subject Matter Expert", "Subject Matter Expert"),
                        ],
                        max_length=50,
                    ),
                ),
                ("profile_info", models.TextField(blank=True)),
                ("user_logo", models.ImageField(blank=True, null=True, upload_to="user_logos/")),
                (
                    "company_id",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="users.company"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", backend.users.managers.UserManager()),
            ],
        ),
    ]
