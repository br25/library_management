from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'student'

    def has_object_permission(self, request, view, obj):
        if request.user.user_role == 'student':
            return True
        return False

class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'librarian'

    def has_object_permission(self, request, view, obj):
        if request.user.user_role == 'librarian':
            return True
        return False

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'teacher'

    def has_object_permission(self, request, view, obj):
        if request.user.user_role == 'teacher':
            return True
        return False

class IsStudentOrTeacher(BasePermission):
    def has_permission(self, request, view):
        return IsStudent().has_permission(request, view) or IsTeacher().has_permission(request, view)
