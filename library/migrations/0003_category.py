# Generated by Django 5.1.2 on 2024-10-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_customuserprofile_deleted_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]
