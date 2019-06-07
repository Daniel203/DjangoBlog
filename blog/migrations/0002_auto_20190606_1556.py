# Generated by Django 2.2.2 on 2019-06-06 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['author', 'created_on', 'body'], name='blog_commen_author_8ce787_idx'),
        ),
    ]
