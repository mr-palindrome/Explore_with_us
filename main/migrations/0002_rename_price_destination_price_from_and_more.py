# Generated by Django 4.0 on 2022-01-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='price',
            new_name='price_from',
        ),
        migrations.AddField(
            model_name='destination',
            name='price_to',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]