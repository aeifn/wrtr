# Generated by Django 2.1.4 on 2018-12-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='heh', max_length=500),
            preserve_default=False,
        ),
    ]
