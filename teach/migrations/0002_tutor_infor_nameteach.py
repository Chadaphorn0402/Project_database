# Generated by Django 3.2.15 on 2022-10-21 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor_infor',
            name='nameteach',
            field=models.CharField(default='', max_length=255),
        ),
    ]
