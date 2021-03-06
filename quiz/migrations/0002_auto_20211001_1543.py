# Generated by Django 3.2.6 on 2021-10-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulity',
            field=models.CharField(choices=[('Khó', 'Khó'), ('Dễ', 'Dễ'), ('Trung bình', 'Trung bình')], max_length=10),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='show_result',
            field=models.CharField(choices=[('Có', 'Có'), ('Không', 'Không')], default='Có', max_length=10),
        ),
    ]
