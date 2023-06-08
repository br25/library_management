from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import User, Student, Librarian, Teacher
from .serializers import StudentSerializer, StudentLoginSerializer, LibrarianSerializer, TeacherSerializer

# Student
class StudentRegistrationAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentLoginAPIView(generics.CreateAPIView):
    serializer_class = StudentLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        if user is not None:
            # Perform any additional logic if needed
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class StudentLogoutAPIView(generics.ListCreateAPIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Successfully logged out'})

# Librarian
class LibrarianRegistrationAPIView(generics.ListCreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

class LibrarianLoginAPIView(generics.ListCreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user is not None:
            login(request, user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LibrarianLogoutAPIView(generics.ListCreateAPIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Successfully logged out'})

# Teacher
class TeacherRegistrationAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherLoginAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user is not None:
            login(request, user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class TeacherLogoutAPIView(generics.ListCreateAPIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Successfully logged out'})
