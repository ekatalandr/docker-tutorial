# Generated by Django 2.1.3 on 2020-06-22 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20200519_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_like',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
