from django.urls import path

from apps.views import UserListView, FreelancerListView, BusinessOwnerListView, SignUpAPIView, LoginAPIView, \
    UserRetrieveAPIView, UserCreateAPIView, UserUpdateAPIView, UserDeleteAPIView, FreelancerDeleteAPIView, \
    FreelancerUpdateAPIView, FreelancerRetrieveAPIView, FreelancerCreateAPIView

urlpatterns = [
    # User url's
    path('user-list/', UserListView.as_view(), name='user-list'),
    path('detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),
    # Freelance url's
    path('freelancer-list/', FreelancerListView.as_view(), name='freelance-list'),
    path('freelancer-detail/<int:pk>/', FreelancerRetrieveAPIView.as_view(), name='freelance-detail'),
    path('freelancer-create/', FreelancerCreateAPIView.as_view(), name='freelance-create'),
    path('freelancer-update/<int:pk>/', FreelancerUpdateAPIView.as_view(), name='freelance-update'),
    path('freelancer-delete/<int:pk>/', FreelancerDeleteAPIView.as_view(), name='freelance-delete'),
    # B owner url's
    path('businees-owner-list/', BusinessOwnerListView.as_view(), name='business-owner-list'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
