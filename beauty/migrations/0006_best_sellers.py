# Generated by Django 5.1.3 on 2024-11-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0005_featured_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Best_sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]