# Generated by Django 4.1.7 on 2023-03-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='username',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateField(editable=False),
        ),
    ]
