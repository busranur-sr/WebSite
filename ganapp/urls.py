from django.urls import path
from . import views
from ganapp.views import signup
from ganapp.views import send_verification_email, verify_email

urlpatterns = [
    path("", views.login_view, name="login"),
    path("signup/", signup, name="signup"),
    path("home/", views.home_view, name="home"),
    path("logout/", views.logout_view, name="logout"),
    path('send-verification-email/', send_verification_email, name='send_verification_email'),
    path('verify-email/<str:uidb64>/<str:token>/', verify_email, name='verify_email'),

    # other paths...
]
