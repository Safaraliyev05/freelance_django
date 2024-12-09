from rest_framework.serializers import ModelSerializer

from apps.models import Freelancer


class FreelanceModelSerializer(ModelSerializer):
    class Meta:
        model = Freelancer
        fields = ['id', ]
