from rest_framework import serializers

from web.models import User, MoneySlotTag, MoneySlot


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneySlotTag
        fields = ('id', 'title')


class MoneySlotSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    amount_spent = serializers.IntegerField()
    user = UserSerializer()
    tags = TagSerializer(many=True)



