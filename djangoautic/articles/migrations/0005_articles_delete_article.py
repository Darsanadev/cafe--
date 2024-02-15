# Generated by Django 4.2.4 on 2023-09-07 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]