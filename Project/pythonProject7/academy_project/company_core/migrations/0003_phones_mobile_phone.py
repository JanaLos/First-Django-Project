# Generated by Django 5.0.3 on 2024-03-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_core', '0002_phones'),
    ]

    operations = [
        migrations.AddField(
            model_name='phones',
            name='mobile_phone',
            field=models.CharField(default='', max_length=9),
        ),
    ]
