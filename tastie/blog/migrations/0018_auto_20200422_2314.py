# Generated by Django 3.0.4 on 2020-04-22 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_date']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comment',
            new_name='active',
        ),
    ]