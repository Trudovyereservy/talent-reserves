from rest_framework.pagination import PageNumberPagination


COACH_PAGE_SIZE = 6


class CoachPagination(PageNumberPagination):
    """
    Переопределение стандартного класса пагинации для произвольного
    задания размера страницы. Для исключения дублирования
    нужно оставить один подобный класс для всех.
    """
    page_size = COACH_PAGE_SIZE
    page_size_query_param = 'limit'
