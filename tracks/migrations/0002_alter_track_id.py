# Generated by Django 4.2.4 on 2023-08-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="track",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
