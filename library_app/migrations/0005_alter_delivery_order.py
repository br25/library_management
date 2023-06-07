# Generated by Django 4.2.1 on 2023-06-07 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library_app", "0004_alter_delivery_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="order",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="library_app.order"
            ),
        ),
    ]