from django.db import models

# Create your models here.
class Problem(models.Model):
    '''Модель для задач с полями, которые описаны в ТЗ'''
    theme = models.CharField(max_length=255, verbose_name='тема')
    number_of_solution = models.IntegerField(verbose_name='количество решений')
    number_of_problem = models.CharField(max_length=255, verbose_name='номер задачи')
    name_of_problem = models.CharField(max_length=255, verbose_name='название задачи')
    problem_complexity = models.IntegerField(verbose_name='сложность задачи')

    def __str__(self):
        return f'{self.theme}, {self.number_of_solution}, {self.number_and_name_of_problem}, {self.problem_complexity}'

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'