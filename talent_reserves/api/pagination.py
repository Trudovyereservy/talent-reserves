from rest_framework.pagination import PageNumberPagination

PAGE_SIZE = 6


class NewsPagination(PageNumberPagination):
    page_size = PAGE_SIZE


class CoachPagination(PageNumberPagination):
    """
    Переопределение стандартного класса пагинации для произвольного
    задания размера страницы. Для исключения дублирования
    нужно оставить один подобный класс для всех.
    """
    page_size = PAGE_SIZE
    page_size_query_param = 'limit'
