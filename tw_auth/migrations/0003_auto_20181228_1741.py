# Generated by Django 2.1.4 on 2018-12-28 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tw_auth', '0002_tweet_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]