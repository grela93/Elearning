# Generated by Django 3.2.6 on 2021-10-03 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_quiz_difficulity'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='docx',
            field=models.FileField(blank=True, default='', null=True, upload_to='quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='difficulity',
            field=models.CharField(choices=[('Khó', 'Khó'), ('Dễ', 'Dễ'), ('Trung bình', 'Trung bình')], max_length=10),
        ),
    ]
