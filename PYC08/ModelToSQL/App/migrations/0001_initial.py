# Generated by Django 3.1 on 2020-08-28 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('b_name', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'Book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=16)),
                ('u_icon', models.ImageField(upload_to='icons')),
            ],
        ),
    ]