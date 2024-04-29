from rest_framework import serializers

from .models import Letter, UserLearning


class LetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Letter
        fields = ['tamil', 'phonetic', 'description', 'sound', 'type', 'id']
        read_only_fields = ['created', 'updated', 'id']

class UserLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLearning
        fields = ['username', 'learning_status', 'id']
        read_only_fields = ['created', 'updated', 'id']