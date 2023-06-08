from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    BookListAPIView,
    BookCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
    OrderListAPIView,
    OrderCreateAPIView,
    OrderRetrieveUpdateDestroyAPIView,
    DeliveryListCreateAPIView,
    DeliveryRetrieveUpdateDestroyAPIView,
    NotificationListAPIView,
    ReturnBookListCreateAPIView,
    ReturnBookRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('', BookListAPIView.as_view(), name='book-list'),
    path('create/', BookCreateAPIView.as_view(), name='book-create'),
    path('<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    path('orders/', OrderListAPIView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-retrieve-update-destroy'),
    path('delivery/', DeliveryListCreateAPIView.as_view(), name='delivery-list-create'),
    path('delivery/<int:pk>/', DeliveryRetrieveUpdateDestroyAPIView.as_view(), name='delivery-retrieve-update-destroy'),
    path('notifications/', NotificationListAPIView.as_view(), name='notification-list'),
    path('return-books/', ReturnBookListCreateAPIView.as_view(), name='return-book-list'),
    path('return-books/<int:pk>/', ReturnBookRetrieveUpdateDestroyAPIView.as_view(), name='return-book-detail'),
]