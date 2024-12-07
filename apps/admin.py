from django.contrib import admin

from apps.models import User, Freelancer, BusinessOwner


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    pass


@admin.register(BusinessOwner)
class BusinessOwnerAdmin(admin.ModelAdmin):
    pass
