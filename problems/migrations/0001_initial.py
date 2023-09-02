# Generated by Django 4.2.4 on 2023-09-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=255, verbose_name='тема')),
                ('number_of_solution', models.IntegerField(verbose_name='количество решений')),
                ('number_and_name_of_problem', models.CharField(max_length=255, verbose_name='номер + название задачи')),
                ('problem_complexity', models.IntegerField(verbose_name='сложность задачи')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
            },
        ),
    ]