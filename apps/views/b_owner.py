from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from apps.models import BusinessOwner
from apps.serializers import BusinessOwnerModelSerializer


@extend_schema(tags=['Business Owner List'])
class BusinessOwnerListView(ListAPIView):
    queryset = BusinessOwner.objects.all()
    serializer_class = BusinessOwnerModelSerializer
