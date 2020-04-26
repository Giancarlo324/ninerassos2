# Generated by Django 2.2.8 on 2020-04-23 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200422_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='stars_count',
        ),
        migrations.AddField(
            model_name='hojavida',
            name='stars_count',
            field=models.DecimalField(decimal_places=1, default=5, max_digits=2),
        ),
    ]
