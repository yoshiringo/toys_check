# Generated by Django 4.2.3 on 2023-07-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0004_toys_freq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toys',
            name='freq',
            field=models.CharField(blank=True, choices=[('たまに', 'たまに'), ('よく', 'よく'), ('いつも', 'いつも')], max_length=50, verbose_name='頻度'),
        ),
    ]
