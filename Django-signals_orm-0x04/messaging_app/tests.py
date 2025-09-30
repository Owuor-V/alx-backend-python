from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification


class SignalTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="alice", password="pass123")
        self.user2 = User.objects.create_user(username="bob", password="pass123")

    def test_notification_created_on_message(self):
        # Create a new message
        msg = Message.objects.create(sender=self.user1, receiver=self.user2, content="Hello Bob!")

        # Check if notification was created
        notification = Notification.objects.get(user=self.user2, message=msg)
        self.assertEqual(notification.user, self.user2)
        self.assertFalse(notification.is_read)
