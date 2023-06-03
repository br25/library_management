from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
    IssuedBookListCreateAPIView,
    IssuedBookRetrieveUpdateDestroyAPIView,
    OrderListCreateAPIView,
)


urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('', BookListCreateAPIView.as_view(), name='book-list'),
    path('<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    path('issued-books/', IssuedBookListCreateAPIView.as_view(), name='issued-book-list'),
    path('issued-books/<int:pk>/', IssuedBookRetrieveUpdateDestroyAPIView.as_view(), name='issued-book-detail'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),

]