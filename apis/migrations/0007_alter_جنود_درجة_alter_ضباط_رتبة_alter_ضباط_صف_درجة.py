# Generated by Django 4.1 on 2023-05-28 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_جنود_درجة_ضباط_رتبة_ضباط_صف_درجة'),
    ]

    operations = [
        migrations.AlterField(
            model_name='جنود',
            name='درجة',
            field=models.CharField(max_length=64, verbose_name='الدرجة'),
        ),
        migrations.AlterField(
            model_name='ضباط',
            name='رتبة',
            field=models.CharField(max_length=64, verbose_name='الرتبة'),
        ),
        migrations.AlterField(
            model_name='ضباط_صف',
            name='درجة',
            field=models.CharField(max_length=64, verbose_name='الدرجة'),
        ),
    ]
