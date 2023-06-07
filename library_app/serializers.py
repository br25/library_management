from rest_framework import serializers
from .models import Category, Book, IssuedBook, Order, Delivery

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class BookSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    available = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'isbn', 'description', 'quantity', 'available', 'category']

    def get_available(self, obj):
        if obj.quantity > 0:
            return obj.available == True
        else:
            return f"Out Of Stock. Quantity: {obj.quantity}"



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
    user = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    book_title = serializers.ReadOnlyField(source='book.title')
    category_name = serializers.ReadOnlyField(source='book.category.name')

    class Meta:
        model = Order
        fields = ['id', 'user', 'email', 'order_date', 'book', 'book_title', 'category_name', 'return_date']

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
    order = OrderSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), write_only=True)

    class Meta:
        model = Delivery
        fields = ['order', 'order_id', 'tracking_number', 'courier', 'delivery_date']

    def validate_order_id(self, order_id):
        # Check if a delivery with the same order_id already exists
        if Delivery.objects.filter(order_id=order_id).exists():
            raise serializers.ValidationError("A delivery with this order already exists.")
        return order_id

    def create(self, validated_data):
        order = validated_data.pop('order_id')
        delivery = Delivery.objects.create(order=order, **validated_data)

        # Delete the associated order
        order.delete()

        return delivery



