# Generated by Django 5.1.3 on 2024-11-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0015_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='best_sellers',
            name='category',
            field=models.CharField(default='best_seller', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='braiding',
            name='category',
            field=models.CharField(default='braiding', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='cleansing',
            name='category',
            field=models.CharField(default='cleansing', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='discounted',
            name='category',
            field=models.CharField(default='discounted', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='new_arrival',
            name='category',
            field=models.CharField(default='new_arival', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='oil',
            name='category',
            field=models.CharField(default='oil', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='treatment',
            name='category',
            field=models.CharField(default='treatment', editable=False, max_length=20),
        ),
    ]