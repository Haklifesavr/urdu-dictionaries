from . import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
# from accounts.views import Registration

app_name = "accounts_urls"

urlpatterns = [
    # path("register/", Registration.as_view()),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
    path("login_redirect/", views.social_login_redirect, name="login_redirect"),
    path("get_tokens/", views.get_tokens, name="get_tokens")
]
