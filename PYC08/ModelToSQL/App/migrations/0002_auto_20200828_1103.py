# Generated by Django 3.1 on 2020-08-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='u_icon',
            field=models.ImageField(upload_to='%Y%m%d/icons'),
        ),
    ]
