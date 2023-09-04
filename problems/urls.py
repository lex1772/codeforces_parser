from django.urls import path

from problems.apps import ProblemsConfig
from problems.views import ProblemListAPIView, ProblemRetrieveAPIView

app_name = ProblemsConfig.name

#Урлы для просмотра задач через API локального сервера
urlpatterns = [
    path('', ProblemListAPIView.as_view(), name='problem_list'),
    path('<int:pk>/', ProblemRetrieveAPIView.as_view(), name='problem'),
]