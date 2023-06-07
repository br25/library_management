from django.db.models import Q
from rest_framework import generics, filters
from .models import Category, Book, Order, Delivery, Notification, ReturnBook
from .serializers import CategorySerializer, BookSerializer, ReturnBookSerializer, OrderSerializer, DeliverySerializer, NotificationSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.filter(is_delivered=False)
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.filter(is_delivered=False)
    serializer_class = OrderSerializer


class DeliveryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class NotificationListAPIView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class ReturnBookListCreateAPIView(generics.ListCreateAPIView):
    queryset = ReturnBook.objects.all()
    serializer_class = ReturnBookSerializer

class ReturnBookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReturnBook.objects.all()
    serializer_class = ReturnBookSerializer