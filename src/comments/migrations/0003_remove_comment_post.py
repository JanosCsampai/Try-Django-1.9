# Generated by Django 2.0.3 on 2018-04-02 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]
