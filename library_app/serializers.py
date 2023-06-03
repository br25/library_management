from rest_framework import serializers
from .models import Category, Book, IssuedBook, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    quantity = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'isbn', 'description', 'quantity', 'available', 'category']

    def get_quantity(self, obj):
        return obj.quantity

class IssuedBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = IssuedBook
        fields = ['id', 'book', 'issued_date', 'return_date', 'fine', 'fine_reason']

    def create(self, validated_data):
        issued_book = IssuedBook.objects.create(**validated_data)
        issued_book.calculate_fine()  # Calculate the fine for the newly issued book
        return issued_book

    def update(self, instance, validated_data):
        instance.return_date = validated_data.get('return_date', instance.return_date)
        instance.fine_reason = validated_data.get('fine_reason', instance.fine_reason)
        instance.save()
        instance.calculate_fine()  # Recalculate the fine for the updated issued book
        return instance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     if not instance.is_completed and validated_data.get('is_completed', False):
    #         instance.is_completed = True
    #         instance.book.quantity -= 1
    #         instance.book.save()
    #     return super().update(instance, validated_data)
