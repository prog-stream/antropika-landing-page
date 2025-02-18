from django.urls import path

from apps.users.views import HomeView, LandingPageView, RegisterView


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('onboarding', LandingPageView.as_view(), name='onboarding'),
    path('', HomeView.as_view(), name='home'),
]
