from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow users to only access their own messages/conversations.
    """

    def has_object_permission(self, request, view, obj):
        # Assuming your message model has a `sender` or `owner` field
        return obj.sender == request.user or obj.receiver == request.user
