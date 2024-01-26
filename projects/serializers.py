from rest_framework import serializers
from .models import Profile, Project, Certificate, CertifyingInstitution


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class NestedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["name"]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = "__all__"

    def create(self, validated_data):
        data = validated_data.pop("certificates")
        institution_data = CertifyingInstitution.objects.create(
            **validated_data
        )

        for certificate in data:
            certificate_data = Certificate.objects.create(
                certifying_institution=institution_data, **certificate
            )
            institution_data.certificates.add(certificate_data)
        return institution_data
