# Generated by Django 4.0.6 on 2022-07-14 02:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("glizzy", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="glizzy",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                error_messages={"unique": "The uuid is not unique."},
                unique=True,
            ),
        ),
    ]
