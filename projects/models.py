from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500),
          ]
      )
    github = models.URLField(
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500),
          ]
      )
    linkedin = models.URLField(
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500),
          ]
      )
    bio = models.TextField(
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500),
          ]
      )
    profile_image = CloudinaryField(blank=True)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500),
          ]
      )
    description = models.TextField(
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500),
          ]
      )
    github_url = models.URLField(
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500),
          ]
      )
    keyword = models.CharField(
      max_length=50,
      validators=[
          MinLengthValidator(1),
          MaxLengthValidator(500),
        ]
      )
    project_image = CloudinaryField(blank=True)
    key_skill = models.CharField(
      max_length=50,
      validators=[
          MinLengthValidator(1),
          MaxLengthValidator(500),
        ]
      )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects"
        )

    def __str__(self) -> str:
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500),
          ]
      )
    url = models.URLField(
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500),
          ]
      )

    def __str__(self) -> str:
        return self.name


class Certificate(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500),
          ]
      )
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates"
      )
    certificate_image = CloudinaryField(blank=True)
    certificate_text = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500),
          ]
      )
    profiles = models.ManyToManyField(
        Profile,
        related_name='certificates',
        )

    def __str__(self) -> str:
        return self.name
