from django.urls import path
from .views import UserProfileView


urlpatterns = [
    path("userprofile/<int:user_id>/", UserProfileView.as_view()),
]
