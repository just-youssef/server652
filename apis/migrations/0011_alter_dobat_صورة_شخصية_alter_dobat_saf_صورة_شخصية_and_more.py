# Generated by Django 4.1 on 2023-05-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0010_alter_dobat_صورة_شخصية'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dobat',
            name='صورة_شخصية',
            field=models.ImageField(default='../media/profiles/no-profile.png', upload_to='profiles/dobat'),
        ),
        migrations.AlterField(
            model_name='dobat_saf',
            name='صورة_شخصية',
            field=models.ImageField(default='../media/profiles/no-profile.png', upload_to='profiles/dobat_saf'),
        ),
        migrations.AlterField(
            model_name='gnod',
            name='صورة_شخصية',
            field=models.ImageField(default='../media/profiles/no-profile.png', upload_to='profiles/gnod'),
        ),
    ]
