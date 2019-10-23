from rest_framework import serializers
from subscriptions.models import Subscription


class SubDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
