# Generated by Django 4.2.3 on 2023-07-28 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0011_tag_remove_toys_tags_toys_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toys',
            name='tags',
        ),
        migrations.AlterModelTable(
            name='toys',
            table=None,
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='toys',
            name='tags',
            field=models.CharField(blank=True, null=True, verbose_name='頻度'),
        ),
    ]
