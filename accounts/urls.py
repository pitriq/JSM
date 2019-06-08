from django.urls import path

from accounts.webservice import (UserConfirmEmailView,
                                 UserEmailConfirmationStatusView)

urlpatterns = [
    path('confirmation/status/', UserEmailConfirmationStatusView),
    path('confirmation/confirm/<uuid:activation_key>', UserConfirmEmailView),
]
