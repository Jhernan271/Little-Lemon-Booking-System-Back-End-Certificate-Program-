# Generated by Django 5.1 on 2024-09-02 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('menu_item_description', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
