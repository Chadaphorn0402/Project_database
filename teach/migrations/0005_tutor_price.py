# Generated by Django 4.1.1 on 2022-10-27 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0004_alter_tutor_pic_alter_tutor_infor_vdo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='price',
            field=models.CharField(default='', max_length=255),
        ),
    ]