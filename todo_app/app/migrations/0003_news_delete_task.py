# Generated by Django 4.1.5 on 2023-02-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_task_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
