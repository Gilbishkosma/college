# Generated by Django 2.1.5 on 2019-02-01 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='imglink',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
