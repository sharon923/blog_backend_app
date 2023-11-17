from rest_framework import serializers
from blogs.models import RegisterModel, BlogModel

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= RegisterModel
        fields =(
            "name",
            "profile",
            "email",
            "password"
        )

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields =(
            "userId",
            "title",
            "message"
        )