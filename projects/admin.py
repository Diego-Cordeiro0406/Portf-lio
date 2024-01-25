from django.contrib import admin
from .models import Profile, Project, Certificate, CertifyingInstitution


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(CertifyingInstitution)
