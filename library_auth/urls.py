from django.urls import path
from . import views

urlpatterns = [
    # Student
    path('student/register/', views.StudentRegistrationAPIView.as_view(), name='student-register'),
    path('student/login/', views.StudentLoginAPIView.as_view(), name='student-login'),
    path('student/logout/', views.StudentLogoutAPIView.as_view(), name='student-logout'),

    # Librarian
    path('librarian/register/', views.LibrarianRegistrationAPIView.as_view(), name='librarian-register'),
    path('librarian/login/', views.LibrarianLoginAPIView.as_view(), name='librarian-login'),
    path('librarian/logout/', views.LibrarianLogoutAPIView.as_view(), name='librarian-logout'),

    # Teacher
    path('teacher/register/', views.TeacherRegistrationAPIView.as_view(), name='teacher-register'),
    path('teacher/login/', views.TeacherLoginAPIView.as_view(), name='teacher-login'),
    path('teacher/logout/', views.TeacherLogoutAPIView.as_view(), name='teacher-logout'),
]
