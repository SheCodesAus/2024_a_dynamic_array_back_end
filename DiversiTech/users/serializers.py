from rest_framework import serializers
from .models import CustomUser
from .validators import validate_unique_username

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer uses a custom validator to ensure case-insensitive uniqueness of usernames. 
    """

    username = serializers.CharField(validators=[validate_unique_username])

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
