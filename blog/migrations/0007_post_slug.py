# Generated by Django 4.1 on 2022-09-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_dislike_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]