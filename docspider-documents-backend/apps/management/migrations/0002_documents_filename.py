# Generated by Django 5.1.4 on 2024-12-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='filename',
            field=models.CharField(default='', help_text='Nome do arquivo com até 100 caractéres', max_length=100, verbose_name='Nome do arquivo'),
        ),
    ]