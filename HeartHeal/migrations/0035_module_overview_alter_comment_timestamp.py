# Generated by Django 4.2.3 on 2023-08-24 06:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeartHeal', '0034_module_video_link_alter_comment_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='overview',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 6, 28, 13, 76018, tzinfo=datetime.timezone.utc)),
        ),
    ]