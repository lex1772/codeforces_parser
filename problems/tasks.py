import requests
from celery import shared_task

from problems.models import Problem


@shared_task
def my_task():
    '''Периодическая задача, которая выполняется раз в один час, подключается к API codeforces и добаввляет новые задачи в базу данных, если они есть'''
    response = requests.get('https://codeforces.com/api/problemset.problems')

    for problem in range(len(response.json()['result']['problems'])):
        try:
            problem_complexity = response.json()['result']['problems'][problem]['points']
        except KeyError:
            problem_complexity = 0
        number_of_solution = response.json()['result']['problemStatistics'][problem]['solvedCount']
        Problem.objects.get_or_create(
            theme=response.json()['result']['problems'][problem]['tags'],
            number_of_solution=number_of_solution,
            number_of_problem=str(response.json()['result']['problems'][problem]['contestId']) +
                              response.json()['result']['problems'][problem]['index'],
            name_of_problem=response.json()['result']['problems'][problem]['name'],
            problem_complexity=problem_complexity,
        )
