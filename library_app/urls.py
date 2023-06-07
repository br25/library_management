from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
    OrderListCreateAPIView,
    OrderRetrieveUpdateDestroyAPIView,
    DeliveryListCreateAPIView,
    DeliveryRetrieveUpdateDestroyAPIView,
    NotificationListAPIView,
    ReturnBookListCreateAPIView,
    ReturnBookRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('', BookListCreateAPIView.as_view(), name='book-list'),
    path('<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-retrieve-update-destroy'),
    path('delivery/', DeliveryListCreateAPIView.as_view(), name='delivery-list-create'),
    path('delivery/<int:pk>/', DeliveryRetrieveUpdateDestroyAPIView.as_view(), name='delivery-retrieve-update-destroy'),
    path('notifications/', NotificationListAPIView.as_view(), name='notification-list'),
    path('return-books/', ReturnBookListCreateAPIView.as_view(), name='return-book-list'),
    path('return-books/<int:pk>/', ReturnBookRetrieveUpdateDestroyAPIView.as_view(), name='return-book-detail'),
]