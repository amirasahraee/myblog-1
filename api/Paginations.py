from rest_framework.pagination import PageNumberPagination


class PublicPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'perPage'
    max_page_size = 12
