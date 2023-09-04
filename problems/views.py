from rest_framework import generics

from problems.models import Problem
from problems.paginators import ProblemPaginator
from problems.serializers import ProblemSerializer


class ProblemListAPIView(generics.ListAPIView):
    '''Контролер для получения списка задач'''
    queryset = Problem.objects.all()
    pagination_class = ProblemPaginator
    serializer_class = ProblemSerializer


class ProblemRetrieveAPIView(generics.RetrieveAPIView):
    '''Контролер для просмотра задачи'''
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer