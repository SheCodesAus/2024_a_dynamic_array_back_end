from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .validators import validate_unique_username

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer uses a custom validator to ensure case-insensitive uniqueness of usernames.
    Django in-built password validation implemented

    """

    username = serializers.CharField(validators=[validate_unique_username])

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}, 'id': {'read_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        try:
            validate_password(password=validated_data['password'], user=user)
        except ValidationError as err:
            user.delete()
            raise serializers.ValidationError({'password': err.messages})    
        return user
    
