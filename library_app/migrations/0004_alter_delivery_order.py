# Generated by Django 4.2.1 on 2023-06-07 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library_app", "0003_remove_delivery_unique_delivery_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="order",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT, to="library_app.order"
            ),
        ),
    ]