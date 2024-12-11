from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from apps.models import BusinessOwner
from apps.permission import IsSuperuser
from apps.serializers import BusinessOwnerModelSerializer


@extend_schema(tags=['Business Owner'])
class BusinessOwnerListView(ListAPIView):
    queryset = BusinessOwner.objects.all()
    serializer_class = BusinessOwnerModelSerializer
    permission_classes = [IsSuperuser, ]


@extend_schema(tags=['Business Owner'])
class BusinessOwnerCreateAPIView(CreateAPIView):
    queryset = BusinessOwner.objects.all()
    serializer_class = BusinessOwnerModelSerializer


@extend_schema(tags=['Business Owner'])
class BusinessOwnerUpdateAPIView(UpdateAPIView):
    queryset = BusinessOwner.objects.all()
    serializer_class = BusinessOwnerModelSerializer


@extend_schema(tags=['Business Owner'])
class BusinessOwnerDeleteAPIView(DestroyAPIView):
    queryset = BusinessOwner.objects.all()
    serializer_class = BusinessOwnerModelSerializer


@extend_schema(tags=['Business Owner'])
class BusinessOwnerRetrieveAPIView(RetrieveAPIView):
    queryset = BusinessOwner.objects.all()
    serializer_class = BusinessOwnerModelSerializer
