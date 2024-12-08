from django.urls import path

from apps.views import UserListView, FreelancerListView, BusinessOwnerListView, SignUpAPIView, LoginAPIView

urlpatterns = [
    path('user-list/', UserListView.as_view(), name='user-list'),
    path('freelancer-list/', FreelancerListView.as_view(), name='freelance-list'),
    path('businees-owner-list/', BusinessOwnerListView.as_view(), name='business-owner-list'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
