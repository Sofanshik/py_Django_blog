# Generated by Django 3.0.5 on 2020-04-03 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_topic_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Date_publish',
            new_name='date_publish',
        ),
    ]
