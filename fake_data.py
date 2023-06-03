import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import django
django.setup()

import random
from faker import Faker
from datetime import datetime
from library_app.models import Category, Book, IssuedBook, Order
from library_auth.models import User, Student, Librarian, Teacher

fake = Faker()


def generate_library_auth_fake_data():
    # Generate fake data for User model
    username = fake.user_name() + '_' + str(fake.random_number(digits=4))
    email = fake.email()
    phone = fake.phone_number()
    address = fake.address()
    user_role = fake.random_element(elements=('student', 'librarian', 'teacher'))

    # Create a User instance with the generated fake data
    user = User.objects.create(username=username, email=email, phone=phone, address=address, user_role=user_role)

    # Generate fake data for Student, Librarian, or Teacher based on user_role
    if user_role == 'student':
        roll_number = fake.random_number(digits=6)
        batch = fake.random_element(elements=('Batch A', 'Batch B', 'Batch C'))
        student = Student.objects.create(user=user, roll_number=roll_number, batch=batch)
        return student
    elif user_role == 'librarian':
        employee_ID = fake.random_number(digits=6)
        employee_role = fake.random_element(elements=('manager', 'staff', 'accounts'))
        librarian = Librarian.objects.create(user=user, employee_ID=employee_ID, employee_role=employee_role)
        return librarian
    elif user_role == 'teacher':
        employee_id = fake.random_number(digits=6)
        department = fake.random_element(elements=('Mathematics', 'Science', 'English'))
        teacher = Teacher.objects.create(user=user, employee_id=employee_id, department=department)
        return teacher

    return user


def generate_library_app_fake_data():
    # Generate fake data for Category model
    categories = ['Fiction', 'Science Fiction', 'Mystery', 'Romance', 'Thriller']
    category_objs = []
    for category_name in categories:
        category = Category.objects.create(name=category_name)
        category_objs.append(category)

    # Generate fake data for Book model
    books = []
    for _ in range(10):
        title = fake.sentence(nb_words=3)
        author = fake.name()
        category = random.choice(category_objs)
        publication_date = fake.date_between(start_date='-10y', end_date=datetime.today().date())
        isbn = fake.isbn13()
        description = fake.paragraph()
        quantity = random.randint(1, 10)
        available = True if quantity > 0 else False
        book = Book.objects.create(
            title=title,
            author=author,
            category=category,
            publication_date=publication_date,
            isbn=isbn,
            description=description,
            quantity=quantity,
            available=available
        )
        books.append(book)

    # Generate fake data for IssuedBook model
    issued_books = []
    for _ in range(5):
        book = random.choice(books)
        issued_date = fake.date_between(start_date='-1y', end_date=datetime.today().date())
        return_date = fake.date_between(start_date=issued_date, end_date=datetime.today().date())
        fine = random.randint(0, 100)
        fine_reason = fake.sentence()
        issued_book = IssuedBook.objects.create(
            book=book,
            issued_date=issued_date,
            return_date=return_date,
            fine=fine,
            fine_reason=fine_reason
        )
        issued_books.append(issued_book)

    # Generate fake data for Order model
    orders = []
    for _ in range(3):
        user = User.objects.order_by('?').first()  # Assuming you have User objects already created
        book = random.choice(books)
        order_date = fake.date_time_between(start_date='-1y', end_date=datetime.today())
        is_completed = random.choice([True, False])
        order = Order.objects.create(
            user=user,
            book=book,
            order_date=order_date,
            is_completed=is_completed
        )
        orders.append(order)

    return {
        'categories': category_objs,
        'books': books,
        'issued_books': issued_books,
        'orders': orders
    }


# Call the function to generate fake data for library_auth models
fake_data = [generate_library_auth_fake_data() for _ in range(20)]

# Call the function to generate fake data for library_app models
fake_library_app_data = generate_library_app_fake_data()

# Access the generated fake data
categories = fake_library_app_data['categories']
books = fake_library_app_data['books']
issued_books = fake_library_app_data['issued_books']
orders = fake_library_app_data['orders']
