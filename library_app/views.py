from django.db.models import Q
from rest_framework import generics, filters
from .models import Category, Book, IssuedBook, Order
from .serializers import CategorySerializer, BookSerializer, IssuedBookSerializer, OrderSerializer

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

class IssuedBookListCreateAPIView(generics.ListCreateAPIView):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedBookSerializer

class IssuedBookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedBookSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def save(self, *args, **kwargs):
        is_completed_changed = self.pk is None or self.__class__.objects.filter(pk=self.pk, is_completed=False).exists()
        super().save(*args, **kwargs)
        if self.is_completed and is_completed_changed:
            self.book.quantity -= 1
            self.book.save()
            print(self.book)