from django.urls import path
from .views import (
    StudentListCreateView, StudentRetrieveUpdateDestroyView,
    LibrarianListCreateView, LibrarianRetrieveUpdateDestroyView,
    TeacherListCreateView, TeacherRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),
    path('librarians/', LibrarianListCreateView.as_view(), name='librarian-list'),
    path('librarians/<int:pk>/', LibrarianRetrieveUpdateDestroyView.as_view(), name='librarian-detail'),
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroyView.as_view(), name='teacher-detail'),
]
