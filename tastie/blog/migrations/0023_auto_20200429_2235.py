# Generated by Django 3.0.4 on 2020-04-29 22:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0022_dislike_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='users',
            field=models.ManyToManyField(related_name='requirement_post_dis_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='users',
            field=models.ManyToManyField(related_name='requirement_post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
