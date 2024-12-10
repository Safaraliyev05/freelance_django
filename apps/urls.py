from django.urls import path

from apps.views import UserListView, FreelancerListView, BusinessOwnerListView, SignUpAPIView, LoginAPIView, \
    UserRetrieveAPIView, UserCreateAPIView, UserUpdateAPIView, UserDeleteAPIView

urlpatterns = [
    # User url's
    path('user-list/', UserListView.as_view(), name='user-list'),
    path('detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),
    # Freelance url's
    path('freelancer-list/', FreelancerListView.as_view(), name='freelance-list'),
    path('businees-owner-list/', BusinessOwnerListView.as_view(), name='business-owner-list'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
