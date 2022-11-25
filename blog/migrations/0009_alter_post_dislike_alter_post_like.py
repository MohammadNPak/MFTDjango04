# Generated by Django 4.1 on 2022-09-22 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_picture'),
        ('blog', '0008_alter_post_dislike_alter_post_like_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_dislike', to='accounts.userprofile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_like', to='accounts.userprofile'),
        ),
    ]