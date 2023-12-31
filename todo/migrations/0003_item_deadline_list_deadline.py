# Generated by Django 4.2.5 on 2023-10-08 04:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_item_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="deadline",
            field=models.DateTimeField(
                blank=True, help_text="Deadline of the item", null=True
            ),
        ),
        migrations.AddField(
            model_name="list",
            name="deadline",
            field=models.DateTimeField(
                blank=True, help_text="Deadline of the list", null=True
            ),
        ),
    ]
