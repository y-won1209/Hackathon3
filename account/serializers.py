from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.core import validators
from rest_framework.validators import UniqueValidator

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'])
            #nickname=validated_data['nickname'])
        user.set_password(validated_data['password'])
        user.save()

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise serializers.ValidationError('잘못된 비밀번호입니다.')
            else:
                token = RefreshToken.for_user(user)
                refresh = str(token)
                access = str(token.access_token)

                data = {
                    'id': user.id,
                    #'nickname': user.nickname ,
                    'access_token': access
                }

                return data
        else:
            raise serializers.ValidationError('존재하지 않는 사용자입니다.')


class ProfileSerializer(serializers.ModelSerializer):
    is_manager = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'is_manager']

    def get_is_manager(self, obj):
        user = self.context['request'].user
        return user.is_authenticated and user.manager

class UsernameUniqueCheckSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, min_length=3, max_length=30, validators=[UniqueValidator(queryset=User.objects.all()), UniqueValidator])

    class Meta:
        model = User
        fields = ['username']