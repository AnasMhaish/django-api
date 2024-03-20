from rest_framework import serializers
from core.models import User,Question,Answer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'