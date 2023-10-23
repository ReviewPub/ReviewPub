from rest_framework import serializers

from .models import Domain, Language, Paper, Review, User


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'user_permissions',
            'is_staff',
            'is_superuser',
            'last_login',
            'date_joined'
        )
        read_only_fields = ('is_active', 'last_login', 'groups', 'id')
        extra_kwargs = {'password': {'write_only': True}}
