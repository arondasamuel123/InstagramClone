# Generated by Django 3.0.4 on 2020-03-09 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_remove_like_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='image_id',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user_id',
            new_name='user',
        ),
    ]
