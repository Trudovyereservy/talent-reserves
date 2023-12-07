from rest_framework.pagination import PageNumberPagination

PAGE_SIZE = 6


class BlogPagination(PageNumberPagination):
    page_size = PAGE_SIZE
    page_size_query_param = 'limit'


class NewsPagination(PageNumberPagination):
    page_size = PAGE_SIZE
    page_size_query_param = 'limit'


class CoachPagination(PageNumberPagination):
    page_size = PAGE_SIZE
    page_size_query_param = 'limit'
