from django.urls import path
from .views import SignUpView,  profileView, ProfileUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profileView, name='profile'),
    path('profile_update/', ProfileUpdate.as_view(), name='profile_update')
]
