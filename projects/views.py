from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Profile, Project, Certificate, CertifyingInstitution
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertificateSerializer,
    CertifyingInstitutionSerializer,
  )


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if request.method == 'GET' and pk is not None:
            profile_data = Profile.objects.get(pk=pk)
            projects = Project.objects.filter(profile=pk)
            projects_formated_list = list()
            for project in projects:
                key_skill_formated = project.key_skill.split(",")
                project_formated = {
                    "name": project.name,
                    "description": project.description,
                    "github_url": project.github_url,
                    "keyword": project.keyword,
                    "key_skill": key_skill_formated,
                    "image": project.project_image
                }
                projects_formated_list.append(project_formated)

            certificates = Certificate.objects.filter(profiles=pk)
            context = {
                "profile": profile_data,
                "projects": projects_formated_list,
                "certificates": certificates,
            }
            return render(request, "profile_detail.html", context)
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
