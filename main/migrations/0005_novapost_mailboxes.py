# Generated by Django 4.1.7 on 2023-04-11 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_offers_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='novapost',
            name='mailboxes',
            field=models.TextField(null=True),
        ),
    ]
