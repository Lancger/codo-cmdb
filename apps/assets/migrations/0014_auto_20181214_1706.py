# Generated by Django 2.1.3 on 2018-12-14 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0013_serverauthrule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverauthrule',
            name='user',
            field=models.CharField(max_length=256),
        ),
    ]