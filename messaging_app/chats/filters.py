import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    # Filter by sender or receiver (user id)
    sender = django_filters.NumberFilter(field_name="sender__id", lookup_expr="exact")
    receiver = django_filters.NumberFilter(field_name="receiver__id", lookup_expr="exact")

    # Filter by date range
    start_date = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    end_date = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Message
        fields = ["sender", "receiver", "start_date", "end_date"]
