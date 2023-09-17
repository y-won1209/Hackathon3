from rest_framework import permissions


class ManagerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.manager:  # manager 값이 False일 경우
            return True
        return False


#class IsAuthorOrReadonly(permissions.BasePermission):
#    def has_permission(self, request, view):
#        return request.user and request.user.is_authenticated

    #def has_object_permission(self, request, view, obj):
    #    if request.method in permissions.SAFE_METHODS:
    #        return True

        return obj.author == request.user
    
#c#lass IsAuthenticated(permissions.BasePermission):
#    def has_permission(self, request, view):
#        return request.user and request.user.is_authenticated