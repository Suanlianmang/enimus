# Generated by Django 3.0.2 on 2021-05-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[(1, 'customer'), (2, 'seller'), (3, 'staff')], max_length=30),
        ),
    ]