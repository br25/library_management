from rest_framework import generics, filters
from .models import Category, Book, Order, Delivery, Notification, ReturnBook
from .serializers import CategorySerializer, BookSerializer, ReturnBookSerializer, OrderSerializer, DeliverySerializer, NotificationSerializer
from library_app.permissions import IsStudent, IsLibrarian, IsTeacher, IsStudentOrTeacher
from rest_framework.permissions import IsAuthenticated

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsLibrarian]

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsLibrarian]

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    permission_classes = [IsAuthenticated, ]

class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    permission_classes = [IsAuthenticated, IsLibrarian]

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.filter(is_delivered=False)
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]

class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.filter(is_delivered=False)
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsStudentOrTeacher]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.filter(is_delivered=False)
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsStudent, IsTeacher]

class DeliveryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated, IsLibrarian]

class DeliveryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated, IsLibrarian]

class NotificationListAPIView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, IsStudent, IsTeacher]

class ReturnBookListCreateAPIView(generics.ListCreateAPIView):
    queryset = ReturnBook.objects.all()
    serializer_class = ReturnBookSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]

class ReturnBookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReturnBook.objects.all()
    serializer_class = ReturnBookSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]
