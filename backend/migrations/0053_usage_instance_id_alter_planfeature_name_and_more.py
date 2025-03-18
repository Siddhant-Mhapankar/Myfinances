# Generated by Django 5.1 on 2024-08-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0052_filestoragefile_file_uri_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="usage",
            name="instance_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="planfeature",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="planfeature",
            name="slug",
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name="subscriptionplan",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="usersubscription",
            name="end_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="usersubscription",
            name="start_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name="UserPlan",
        ),
    ]
