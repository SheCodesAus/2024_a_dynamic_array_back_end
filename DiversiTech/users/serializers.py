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
        self.validate_user_password(user, validated_data['password'])
        return user

    def validate_user_password(self, user, password):
        try:
            validate_password(password=password, user=user)
        except ValidationError as err:
            user.delete()
            raise serializers.ValidationError({'password': err.messages})    
        
    
class CustomUserEditSerializer(serializers.ModelSerializer):
    """
    This is used for user detail updates to avoid error when username is unchanged.

    """
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}, 'id': {'read_only': True}}


class UserPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=50, write_only=True, required=True)
    new_password = serializers.CharField(max_length=50, write_only=True, required=True)
    new_password_confirmed = serializers.CharField(max_length=50, write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({'old_password': 'Your old password was entered incorrectly.'})
        return value
    
    def validate(self, data):
        if data['new_password'] != data['new_password_confirmed']:
            raise serializers.ValidationError({'new_password_confirmed': 'The two password fields did not match'})
        validate_password(data['new_password'], self.context['request'].user)
        return data
    
    def save(self, **kwargs):
        password = self.validated_data['new_password']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user
