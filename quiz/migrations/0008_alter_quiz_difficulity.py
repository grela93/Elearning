# Generated by Django 3.2.6 on 2021-10-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_alter_quiz_difficulity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulity',
            field=models.CharField(choices=[('Trung bình', 'Trung bình'), ('Dễ', 'Dễ'), ('Khó', 'Khó')], max_length=10),
        ),
    ]