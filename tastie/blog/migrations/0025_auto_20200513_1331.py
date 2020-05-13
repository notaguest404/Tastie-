# Generated by Django 3.0.4 on 2020-05-13 13:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='active',
            new_name='approved_comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_on',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
