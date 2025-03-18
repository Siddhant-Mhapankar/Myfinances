# Generated by Django 5.1 on 2024-08-28 14:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0053_usage_instance_id_alter_planfeature_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TransferUsage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("amount_in_MB", models.DecimalField(decimal_places=2, max_digits=10)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("feature", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="backend.planfeature")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="StorageUsage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("file_uri_path", models.CharField(max_length=255)),
                ("size_in_MB", models.DecimalField(decimal_places=8, max_digits=10)),
                ("start_time", models.DateTimeField(auto_now_add=True)),
                ("end_time", models.DateTimeField(blank=True, null=True)),
                ("feature", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="backend.planfeature")),
                (
                    "organization",
                    models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="backend.organization"),
                ),
                (
                    "user",
                    models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "abstract": False,
                "constraints": [
                    models.CheckConstraint(
                        check=models.Q(
                            models.Q(("organization__isnull", False), ("user__isnull", True)),
                            models.Q(("organization__isnull", True), ("user__isnull", False)),
                            _connector="OR",
                        ),
                        name="backend_storageusage_check_user_or_organization",
                    )
                ],
            },
        ),
    ]
