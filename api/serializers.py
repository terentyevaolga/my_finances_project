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


class MoneySlotSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(queryset=MoneySlotTag.objects.all(), many=True, write_only=True)

    def save(self, **kwargs):
        tags = self.validated_data.pop("tag_ids")
        self.validated_data['user_id'] = self.context['request'].user.id
        instance = super().save(**kwargs)
        instance.tags.set(tags)
        return instance

    class Meta:
        model = MoneySlot
        fields = ('id', 'title', 'amount_spent', 'tags', 'user', 'tag_ids')





