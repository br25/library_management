# Generated by Django 4.2.1 on 2023-06-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library_app", "0003_remove_order_is_completed_book_is_buy_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="is_buy",
        ),
        migrations.AddField(
            model_name="order",
            name="is_buy",
            field=models.BooleanField(default=False),
        ),
    ]