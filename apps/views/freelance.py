from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from apps.models import Freelancer
from apps.serializers import FreelanceModelSerializer


@extend_schema(tags=['Freelancers List'])
class FreelancerListView(ListAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelanceModelSerializer
