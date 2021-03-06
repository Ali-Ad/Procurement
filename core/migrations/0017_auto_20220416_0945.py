# Generated by Django 3.1.1 on 2022-04-16 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20220414_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(related_name='order_item_order', to='core.OrderItem'),
        ),
    ]
