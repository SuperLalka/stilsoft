from rest_framework import permissions


class PassengerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and
                    request.user.check_group('passenger'))


class DriverPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and
                    request.user.check_group('driver'))


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and
                    request.user.check_group('admin'))
