# Generated by Django 4.2.1 on 2023-05-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='products.orderitem'),
        ),
    ]