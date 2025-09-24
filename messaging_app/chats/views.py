from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsOwner


# class ConversationViewSet(viewsets.ModelViewSet):
#     queryset = Conversation.objects.all().prefetch_related("participants", "message_set")
#     serializer_class = ConversationSerializer
#
#     def create(self, request, *args, **kwargs):
#         participant_ids = request.data.get("participants", [])
#         if not participant_ids:
#             return Response(
#                 {"error": "Participants list is required"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#
#         conversation = Conversation.objects.create()
#         conversation.participants.set(User.objects.filter(user_id__in=participant_ids))
#         conversation.save()
#
#         serializer = self.get_serializer(conversation)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Message.objects.all().select_related("sender", "conversation")
#     serializer_class = MessageSerializer
#
#     def create(self, request, *args, **kwargs):
#         conversation_id = request.data.get("conversation")
#         sender_id = request.data.get("sender")
#         body = request.data.get("message_body")
#
#         if not (conversation_id and sender_id and body):
#             return Response(
#                 {"error": "conversation, sender and message_body are required"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#
#         try:
#             conversation = Conversation.objects.get(conversation_id=conversation_id)
#             sender = User.objects.get(user_id=sender_id)
#         except (Conversation.DoesNotExist, User.DoesNotExist):
#             return Response(
#                 {"error": "Invalid conversation or sender"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#
#         message = Message.objects.create(
#             conversation=conversation, sender=sender, message_body=body
#         )
#
#         serializer = self.get_serializer(message)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsOwner]