# Generated by Django 2.1.2 on 2018-10-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181020_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='videoDwldURL',
        ),
        migrations.AddField(
            model_name='document',
            name='fileUpload',
            field=models.FileField(default='documents/defaultBonusWords.txt', upload_to='documents/'),
        ),
    ]