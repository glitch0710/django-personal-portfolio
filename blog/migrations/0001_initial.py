# Generated by Django 4.0 on 2021-12-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('post_desc', models.TextField()),
            ],
        ),
    ]
