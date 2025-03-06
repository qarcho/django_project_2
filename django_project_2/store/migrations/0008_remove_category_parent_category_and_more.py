# Generated by Django 5.1.6 on 2025-03-05 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0007_rename_category_db_category_parent_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="parent_category",
        ),
        migrations.RemoveField(
            model_name="product",
            name="description",
        ),
        migrations.AddField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.category",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.category",
            ),
        ),
    ]
