# Generated by Django 3.1 on 2020-08-13 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='p_hobby',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
