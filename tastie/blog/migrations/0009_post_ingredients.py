# Generated by Django 3.0.4 on 2020-04-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_servings'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ingredients',
            field=models.TextField(default='Ingredients'),
        ),
    ]