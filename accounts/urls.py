from django.urls import path, include
from accounts.views import account_signup_view, helloView, profile

urlpatterns = [
    path("", view=helloView),
    path("accounts/signup/", view=account_signup_view, name="hello"),
    path("accounts/profile/", view=profile, name="profile"),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("allauth.socialaccount.urls")),
]
