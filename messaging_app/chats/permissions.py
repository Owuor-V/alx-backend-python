
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow users to only access their own messages/conversations.
    """

    def has_object_permission(self, request, view, obj):
        # Assuming your messaging model has a `sender` or `owner` field
        return obj.sender == request.user or obj.receiver == request.user

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allow only:
    - Authenticated users
    - Participants of a conversation to send, view, update, or delete messages
    """

    def has_permission(self, request, view):
        # ✅ Check 1: Only authenticated users can access API
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Assumes:
        - Message model has a ForeignKey to Conversation
        - Conversation has ManyToMany field `participants` to User
        """
        user = request.user
        return user in obj.conversation.participants.all()
