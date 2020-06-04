# Generated by Django 3.0.4 on 2020-04-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='method',
            field=models.TextField(default='Method'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(default='Small Description', max_length=200),
        ),
    ]