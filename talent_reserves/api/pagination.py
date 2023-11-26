from rest_framework.pagination import PageNumberPagination

PAGE_SIZE = 3


class NewsPagination(PageNumberPagination):
    page_size = PAGE_SIZE
    page_size_query_param = 'limit'
