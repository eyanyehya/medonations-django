# Generated by Django 5.0 on 2024-02-18 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medonations_backend', '0004_rename_date_blog_date_published_blog_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subTitle',
            field=models.CharField(default='sub title', max_length=300),
            preserve_default=False,
        ),
    ]
