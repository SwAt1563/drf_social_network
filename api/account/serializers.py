from account.models import UserAccount
from user_profile.models import Profile
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=True,
                                     validators=[UniqueValidator(queryset=UserAccount.objects.all())])
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=UserAccount.objects.all())])
    password = serializers.CharField(required=True, write_only=True,
                                     validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = UserAccount
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attr):
        if attr['password'] != attr['password2']:
            raise serializers.ValidationError(
                {'password': 'password fields not match'},
            )
        return attr

    def create(self, validated_data):
        user = UserAccount.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(
            user=user,
        )
        return user

