# Generated by Django 5.1.1 on 2024-09-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_topic_view_alter_post_massage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited_dt',
            field=models.DateTimeField(null=True),
        ),
    ]
