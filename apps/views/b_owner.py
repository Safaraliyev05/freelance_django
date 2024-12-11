from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView

from apps.models import BusinessOwner
from apps.permission import IsSuperuser
from apps.serializers import BusinessOwnerModelSerializer


@extend_schema(tags=['Business Owner List'])
class BusinessOwnerListView(ListAPIView):
    queryset = BusinessOwner.objects.all()
    serializer_class = BusinessOwnerModelSerializer
    permission_classes = [IsSuperuser, ]


@extend_schema(tags=['Freelancer Create'])
class UserCreateAPIView(CreateAPIView):
    queryset = BusinessOwner.objects.all()
    serializer_class = BusinessOwnerModelSerializer
