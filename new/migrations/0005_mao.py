# Generated by Django 2.0.5 on 2018-05-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0004_article_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=100)),
                ('arti', models.TextField()),
            ],
        ),
    ]
