# Generated by Django 4.2.4 on 2023-10-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_rename_category_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slider',
            field=models.BooleanField(choices=[(0, 'در اسلایدر نباشد'), (1, 'در اسلایدر باشد')], default=False),
        ),
    ]
