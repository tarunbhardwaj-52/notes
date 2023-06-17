# Generated by Django 4.2.2 on 2023-06-16 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('audio', models.FileField(blank=True, null=True, upload_to='audio/')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
