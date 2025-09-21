from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Conversations:
    - list all conversations
    - create new conversation with participants
    - view a single conversation (with nested messages)
    """

    queryset = Conversation.objects.all().prefetch_related("participants", "message_set")
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new conversation with participants.
        Expects: {"participants": [user_id1, user_id2, ...]}
        """
        participant_ids = request.data.get("participants", [])
        if not participant_ids:
            return Response(
                {"error": "Participants list is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        conversation = Conversation.objects.create()
        conversation.participants.set(User.objects.filter(user_id__in=participant_ids))
        conversation.save()

        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Messages:
    - list all messages
    - create/send message to a conversation
    """

    queryset = Message.objects.all().select_related("sender", "conversation")
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        """
        Send a message to a conversation.
        Expects: {"conversation": conversation_id, "sender": user_id, "message_body": "text"}
        """
        conversation_id = request.data.get("conversation")
        sender_id = request.data.get("sender")
        body = request.data.get("message_body")

        if not (conversation_id and sender_id and body):
            return Response(
                {"error": "conversation, sender and message_body are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            conversation = Conversation.objects.get(conversation_id=conversation_id)
            sender = User.objects.get(user_id=sender_id)
        except (Conversation.DoesNotExist, User.DoesNotExist):
            return Response(
                {"error": "Invalid conversation or sender"},
                status=status.HTTP_404_NOT_FOUND,
            )

        message = Message.objects.create(
            conversation=conversation, sender=sender, message_body=body
        )

        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
