# Generated by Django 4.1 on 2023-05-28 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_ضباط_ضباط_صف_جنود_صورة_شخصية'),
    ]

    operations = [
        migrations.AddField(
            model_name='جنود',
            name='درجة',
            field=models.CharField(default='جندى', max_length=64, verbose_name='الدرجة'),
        ),
        migrations.AddField(
            model_name='ضباط',
            name='رتبة',
            field=models.CharField(default='ملازم', max_length=64, verbose_name='الرتبة'),
        ),
        migrations.AddField(
            model_name='ضباط_صف',
            name='درجة',
            field=models.CharField(default='عريف', max_length=64, verbose_name='الدرجة'),
        ),
    ]
