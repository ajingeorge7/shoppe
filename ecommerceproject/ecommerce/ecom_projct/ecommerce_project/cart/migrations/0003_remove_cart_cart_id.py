# Generated by Django 4.2.1 on 2023-09-30 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_id',
        ),
    ]
