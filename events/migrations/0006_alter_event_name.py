# Generated by Django 4.2.5 on 2023-09-26 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_eventlocation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Event Name'),
        ),
    ]