# Generated by Django 4.2.3 on 2023-08-26 01:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeartHeal', '0037_alter_comment_timestamp_alter_meeting_link_meeting_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='doc_profile',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 26, 1, 8, 24, 857130, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='practice',
            name='timestamp',
            field=models.DateField(default=datetime.date(2023, 8, 26)),
        ),
    ]