# Generated by Django 3.1 on 2020-08-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_num', models.CharField(max_length=16, unique=True)),
                ('o_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
