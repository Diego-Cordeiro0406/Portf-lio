from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


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
