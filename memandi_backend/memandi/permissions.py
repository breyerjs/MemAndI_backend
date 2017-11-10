from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Handles permissions for users.  The basic rules are
        - owner may GET, PUT, POST, DELETE
        - no one else can access
    """
    def has_permission(self, request, view):
        return self._route_authenticated_correctly(request, view)

    def _route_authenticated_correctly(self, request, view):
        route_user_id = view.kwargs.get('user_id')
        if route_user_id is None:
            return True
        return str(request.user.id) == view.kwargs['user_id']
