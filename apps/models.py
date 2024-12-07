from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, TextChoices, ForeignKey, CASCADE


class User(AbstractUser):
    class Type(TextChoices):
        FREELANCER = 'freelancer', 'Freelancer'
        BUSINESS_OWNER = 'business owner', 'Business Owner'

    phone_number = CharField(max_length=255, null=True, unique=True)
    role = CharField(max_length=20, choices=Type.choices, default=Type.FREELANCER)

    def __str__(self):
        return self.username


class Education(Model):
    pass


class Project(Model):
    pass


class Freelancer(Model):
    user = ForeignKey(User, CASCADE)
    education = ForeignKey(Education, CASCADE, null=True, blank=True)
    project = ForeignKey(Project, CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username


class BusinessOwner(Model):
    user = ForeignKey(User, CASCADE)

    def __str__(self):
        return self.user.username
