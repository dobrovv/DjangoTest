# Generated by Django 2.0.1 on 2018-01-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20180130_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='username',
            field=models.CharField(default='Unknown User', max_length=128),
        ),
    ]
