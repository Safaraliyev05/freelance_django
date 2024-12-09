from rest_framework.serializers import ModelSerializer

from apps.models import BusinessOwner


class BusinessOwnerModelSerializer(ModelSerializer):
    class Meta:
        model = BusinessOwner
        fields = ['id', ]
