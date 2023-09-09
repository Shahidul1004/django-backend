from django.urls import path, include


from accounts.views import account_signup_view

# from allauth.account.views import SignupView, LoginView, ConfirmEmailView, EmailView, PasswordChangeView, PasswordSetView, PasswordResetView, PasswordResetDoneView, PasswordResetFromKeyView
# from allauth.account.views import PasswordResetFromKeyDoneView,LogoutView, AccountInactiveView, EmailVerificationSentView
urlpatterns = [
    path("accounts/signup/", view=account_signup_view),
    path('accounts/', include('allauth.urls')),
]