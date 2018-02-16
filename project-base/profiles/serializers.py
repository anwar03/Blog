from rest_framework import serializers

from .models import User, UserFeed


class UserSerializer(serializers.ModelSerializer):
    """User profile serializer"""

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'gender', 'password']
        #read_only_fields = ('id', 'is_active', 'is_superuser', 'is_staff', 'date_joined')
        extra_kwargs = {'password': {'write_only': True }}

    def create(self, validated_data):
        """create and return user profile."""
        
        user = User(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone_number = validated_data['phone_number'],
            gender = validated_data['gender']
        )

        user.set_password(validated_data['password'])
        user.save()


        return user

class FeedSerializer(serializers.ModelSerializer):
    """User Feed serializer."""

    class Meta:
        model = UserFeed
        fields = ('id', 'user', 'status_text', 'created_on')
        extra_kwargs = {'user': {'read_only': True }}


    