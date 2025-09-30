from django.db import models
from django.contrib.auth.models import User


class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        """
        Returns unread messages for a given user.
        Optimized with .only() to fetch only necessary fields.
        """
        return (
            self.get_queryset()
            .filter(receiver=user, read=False)
            .only("id", "sender", "receiver", "content", "timestamp")
        )


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)

    # ✅ Threaded conversations (from previous task)
    parent_message = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies"
    )

    # ✅ New field for read/unread tracking
    read = models.BooleanField(default=False)

    # ✅ Default + custom manager
    objects = models.Manager()  # default
    unread = UnreadMessagesManager()  # custom

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.content[:30]}"

    def get_all_replies(self):
        """
        Recursive function to fetch all replies in a threaded format.
        """
        replies = []
        for reply in self.replies.all().select_related("sender", "receiver").prefetch_related("replies"):
            replies.append(reply)
            replies.extend(reply.get_all_replies())
        return replies


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="notifications")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - Message ID {self.message.id}"


class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="histories")
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for Message ID {self.message.id} at {self.edited_at}"
