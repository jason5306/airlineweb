# Generated by Django 4.1.3 on 2022-12-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0014_alter_order_survery_q4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='survery_Q4',
        ),
        migrations.AddField(
            model_name='order',
            name='survery_Q4_1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='survery_Q4_2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='survery_Q4_3',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='survery_Q4_4',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='survery_Q4_5',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
