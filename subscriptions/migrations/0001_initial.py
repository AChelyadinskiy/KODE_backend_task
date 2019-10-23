# Generated by Django 2.2.6 on 2019-10-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('min_price', models.FloatField(blank=True, null=True)),
                ('max_price', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]