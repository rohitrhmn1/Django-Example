from rest_framework.permissions import IsAuthenticated


class SamplePermission(IsAuthenticated):
    def has_permission(self, request, view):
        return False


class NewPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return True
