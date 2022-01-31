from rest_framework.pagination import PageNumberPagination

class FavoritesPagination(PageNumberPagination):
    page_size = 2