from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from problems.models import Problem


# Create your tests here.
class ProblemTestCase(APITestCase):
    # Тесты для привычек
    def setUp(self) -> None:
        # Создание привычки и пользователя для тестирования, авторизация пользователя через токен
        self.problem = Problem.objects.create(
            theme='math',
            number_of_solution=210,
            number_of_problem='514A',
            name_of_problem='Aa',
            problem_complexity=1000,
        )

    def test_get_list(self):
        # Получение списка привычек и сравнение с действием первой привычки
        response = self.client.get(
            reverse('problems:problem_list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['theme'], 'math')

    def test_habit_detail(self):
        # Просмотр привычки
        response = self.client.get(
            reverse('problems:problem', kwargs={'pk': self.problem.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)