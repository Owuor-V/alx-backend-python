
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow users to only access their own messages/conversations.
    """

    def has_object_permission(self, request, view, obj):
        # Assuming your message model has a `sender` or `owner` field
        return obj.sender == request.user or obj.receiver == request.user

class IsParticipantOfConversation(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Assumes:
        - Message model has a `conversation` ForeignKey
        - Conversation model has `participants` (ManyToMany to User)
        """
        user = request.user
        return user in obj.conversation.participants.all()
