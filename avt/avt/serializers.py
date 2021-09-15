from rest_framework import serializers


class AGroupSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.name')

    class Meta:
        fields = (
            'id',
            'group_id',
            'group_name',
            'wid',
        )


class AGSenderSeriailzer(serializers.Serializer):
    content = serializers.CharField(min_length=1, max_length=2048)