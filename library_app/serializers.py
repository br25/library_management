from rest_framework import serializers
from .models import Category, Book, Order, Delivery, Notification, ReturnBook

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    available = serializers.SerializerMethodField()
    isbn = serializers.CharField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'isbn', 'description', 'quantity', 'available', 'category']

    def get_available(self, obj):
        if obj.quantity > 0:
            return obj.available == True
        else:
            return f"Out Of Stock. Quantity: {obj.quantity}"

    def validate_isbn(self, value):
        if value and (len(value) != 13 or not value.isdigit()):
            raise serializers.ValidationError("ISBN must be a 13-digit number")
        return value

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    book_title = serializers.ReadOnlyField(source='book.title')
    category_name = serializers.ReadOnlyField(source='book.category.name')
    is_delivered = serializers.BooleanField(read_only=True)


    class Meta:
        model = Order
        fields = ['id', 'user', 'email', 'order_date', 'book', 'book_title', 'category_name', 'return_date', 'is_delivered']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

    def validate(self, attrs):
        user = self.context['request'].user
        book = attrs['book']

        if Order.objects.filter(user=user, book=book).exists():
            raise serializers.ValidationError("You have already ordered this book.")

        return attrs

class DeliverySerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.filter(is_delivered=False))
    book_name = serializers.SerializerMethodField()

    class Meta:
        model = Delivery
        fields = ['order', 'order_id', 'tracking_number', 'courier', 'delivery_date', 'book_name']

    def get_order(self, obj):
        return OrderSerializer(obj.order).data

    def get_book_name(self, obj):
        return obj.order.book.title if obj.order.book else ''

    def create(self, validated_data):
        order = validated_data.pop('order_id')
        delivery = Delivery.objects.create(order=order, **validated_data)

        # Decrease the book quantity by 1
        book = order.book
        if book:
            book.quantity -= 1
            book.save()

        order.is_delivered = True
        order.save()

        return delivery



class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Notification
        fields = ['message', 'user']

class ReturnBookSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    book_name = serializers.CharField(source='delivery.order.book.title', read_only=True)
    delivery = serializers.PrimaryKeyRelatedField(queryset=Delivery.objects.all())

    class Meta:
        model = ReturnBook
        fields = ['id', 'user', 'user_name', 'book_name', 'delivery', 'fine', 'fine_reason']

    def create(self, validated_data):
        delivery = validated_data['delivery']

        # Increase the book quantity by 1
        book = delivery.order.book
        if book:
            book.quantity += 1
            book.save()

        return ReturnBook.objects.create(**validated_data)
        