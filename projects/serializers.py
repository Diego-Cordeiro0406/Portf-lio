from rest_framework import serializers
from .models import Profile, Project


# class AdminProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'

#     def create(self, validated_data):
#         request = self.context.get('request')
#         if request and request.user.is_superuser:
#             return super().create(validated_data)
#         raise serializers.ValidationError(
#             "Você não tem permissão para criar fornecedores."
#           )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
