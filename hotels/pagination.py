from rest_framework.pagination import PageNumberPagination


class PaginationList(PageNumberPagination):
    page_size = 5
