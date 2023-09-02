import requests
from celery import shared_task

from problems.models import Problem


@shared_task
def my_task():
    stats = {}
    response = requests.get('https://codeforces.com/api/problemset.problems')

    for problem in range(len(response.json()['result']['problems'])):
        print(response.json()['result']['problems'][problem])
        print(response.json()['result']['problemStatistics'][problem])
        problem_complexity = response.json()['result']['problemStatistics'][problem]['solvedCount']
        print(problem_complexity)
        print('---')
        Problem.objects.get_or_create(
            theme=response.json()['result']['problems'][problem]['tags'],
            number_of_solution=stats.get(str(response.json()['result']['problems'][problem]['contestId']) +
                                         response.json()['result']['problems'][problem]['index'], 0),
            number_of_problem=str(response.json()['result']['problems'][problem]['contestId']) +
                              response.json()['result']['problems'][problem]['index'],
            name_of_problem=response.json()['result']['problems'][problem]['name'],
            problem_complexity=problem_complexity,
        )
