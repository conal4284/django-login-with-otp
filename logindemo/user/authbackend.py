from django.contrib.auth.backends import BaseBackend
from user.models import CustomUser
from django.db.models import Q


class CustomAuthBackend(BaseBackend):

    def authenticate(self, request, mobile_number, otp):
        try:
            custom_user = CustomUser.objects.get(Q(mobile_number=mobile_number) & Q(otp=otp))
            return custom_user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None