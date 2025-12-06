from django.urls import path, include
from .views import (UserProfileListAPIView, UserProfileDetailAPIView,
                    PropertyListAPIView, PropertyDetailAPIView, PropertyViewSet,
                    ReviewCreateAPIView, ReviewEditAPIView,
                    BookingViewSet, RegisterView, CustomLoginView,
                    LogoutView)
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'property_create', PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('properties/', PropertyListAPIView.as_view(), name='property_list'),
    path('properties/<int:pk>/', PropertyDetailAPIView.as_view(), name='property_detail'),
    path('reviews/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('reviews/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit'),
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),
]