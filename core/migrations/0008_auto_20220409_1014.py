# Generated by Django 3.1.1 on 2022-04-09 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220409_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
