# Generated by Django 3.1.8 on 2021-04-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(default='sexuality', max_length=255),
        ),
    ]
