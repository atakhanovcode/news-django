# Generated by Django 4.1.5 on 2023-02-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
