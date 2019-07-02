# Generated by Django 2.2.1 on 2019-07-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='connection_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_address', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=150)),
                ('response_Time', models.CharField(max_length=50)),
                ('checked', models.BooleanField(default=True)),
                ('datetime_check', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]