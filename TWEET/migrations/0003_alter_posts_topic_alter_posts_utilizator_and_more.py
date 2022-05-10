# Generated by Django 4.0.4 on 2022-04-29 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TWEET', '0002_posts_aprecieri_posts_topic_posts_utilizator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='topic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='TWEET.topics'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='utilizator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='User_Post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topics',
            name='board',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='TWEET.board'),
        ),
    ]
