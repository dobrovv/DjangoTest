# Generated by Django 2.0.1 on 2018-01-30 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20180129_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
