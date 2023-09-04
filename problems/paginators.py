from rest_framework.pagination import PageNumberPagination


# Создаем постраничный вывод для задач по 10 шт на страницу
class ProblemPaginator(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 50