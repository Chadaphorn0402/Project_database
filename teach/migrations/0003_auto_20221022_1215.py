# Generated by Django 3.2.15 on 2022-10-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0002_tutor_infor_nameteach'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/piclocated'),
        ),
        migrations.AlterField(
            model_name='tutor_infor',
            name='VDO',
            field=models.FileField(blank=True, upload_to='static/video'),
        ),
    ]