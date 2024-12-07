from django.db.models import Model, CharField, TextChoices, ForeignKey, CASCADE


class User(Model):
    class Type(TextChoices):
        FREELANCER = 'freelancer', 'Freelancer'
        BUSINESS_OWNER = 'business owner', 'Business Owner'

    firstname = CharField(max_length=255, null=True)
    lastname = CharField(max_length=255, null=True)
    username = CharField(max_length=255, null=True, unique=True)
    email = CharField(max_length=255, null=True, unique=True)
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
    education = ForeignKey(Education, CASCADE)
    project = ForeignKey(Project, CASCADE)


class BusinessOwner(Model):
    user = ForeignKey(User, CASCADE)
