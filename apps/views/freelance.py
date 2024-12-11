from drf_spectacular.utils import extend_schema
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from apps.models import Freelancer
from apps.permission import IsSuperuser
from apps.serializers import FreelanceModelSerializer


@extend_schema(tags=['Freelancer'])
class FreelancerListView(ListAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelanceModelSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['username', ]
    permission_classes = [IsSuperuser, ]


@extend_schema(tags=['Freelancer'])
class FreelancerCreateAPIView(CreateAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelanceModelSerializer


@extend_schema(tags=['Freelancer'])
class FreelancerUpdateAPIView(UpdateAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelanceModelSerializer


@extend_schema(tags=['Freelancer'])
class FreelancerDeleteAPIView(DestroyAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelanceModelSerializer


@extend_schema(tags=['Freelancer'])
class FreelancerRetrieveAPIView(RetrieveAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelanceModelSerializer
