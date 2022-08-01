from django.urls import path
from user import views
from django.conf import settings

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('otp/', views.OTPView.as_view(), name='otp'),
]