# Generated by Django 4.1.5 on 2023-02-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_news_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default='../static/images/win-xp-background.jpg', upload_to=''),
        ),
    ]
