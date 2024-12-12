from rest_framework import serializers
from .models import PersonalRecord


class PersonalRecordSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = PersonalRecord
        fields = [
            'id', 'owner', 'is_owner', 'exercise', 'weight',
            'reps', 'date_achieved', 'notes'
            ]
        read_only_fields = ['id', 'owner']
