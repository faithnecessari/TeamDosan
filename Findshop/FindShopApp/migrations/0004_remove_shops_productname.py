# Generated by Django 3.0.5 on 2021-12-09 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FindShopApp', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shops',
            name='productName',
        ),
    ]