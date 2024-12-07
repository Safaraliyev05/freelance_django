from drf_spectacular.utils import extend_schema
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView

from apps.models import User
from apps.serializers import UserModelSerializer


@extend_schema(tags=['Users List'])
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['username', ]


@extend_schema(tags=['Users Create'])
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
