from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Profile(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(1), MaxLengthValidator(500)]
      )
    github = models.URLField(
        validators=[MinLengthValidator(1), MaxLengthValidator(500)]
      )
    linkedin = models.URLField(
        validators=[MinLengthValidator(1), MaxLengthValidator(500)]
      )
    bio = models.TextField(
        validators=[MinLengthValidator(1), MaxLengthValidator(500)]
      )

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500)
          ]
      )
    description = models.TextField(
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500)
          ]
      )
    github_url = models.URLField(
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(500)
          ]
      )
    keyword = models.CharField(
      max_length=50,
      validators=[
          MinLengthValidator(1),
          MaxLengthValidator(500)
        ]
      )
    key_skill = models.CharField(
      max_length=50,
      validators=[
          MinLengthValidator(1),
          MaxLengthValidator(500)
        ]
      )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
