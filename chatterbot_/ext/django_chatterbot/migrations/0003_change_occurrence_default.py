# Generated by Django 1.9 on 2016-12-12 00:06
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chatterbot', '0002_statement_extra_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='occurrence',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
