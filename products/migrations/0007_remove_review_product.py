# Generated by Django 3.2.9 on 2022-01-26 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_review_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
    ]
