from email import message
from random import random
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import RedirectView, View
from django.conf import settings
from django.contrib.auth import logout as auth_logout
from user.models import CustomUser, send_otp
from user.forms import CustomUserCreationForm, LoginFormView, OTPForm
import random
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q


class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('otp')
    template_name = 'register/register.html'

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'register/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        first_name = request.POST.get('name')
        mobile_number = request.POST.get('mobile')
        email = request.POST.get('email')
        print(mobile_number, " -- ", email)

        custom_user = CustomUser.objects.filter(Q(mobile_number=mobile_number) | Q(email=email)).first()
        if custom_user:
            messages.error(request, "Mobile Number or Email already registered")
            return render(request, self.template_name, context={'form':form, 'messsage':message})
        else:
            otp = str(random.randint(100000, 999999))
            print(otp, "otp when generated")
            custom_user = CustomUser.objects.create(first_name=first_name, mobile_number=mobile_number, email=email, otp=otp)
            custom_user.save()
            send_login_otp(mobile_number, otp)
            request.session['mobile_number'] = mobile_number
            return redirect('otp')


    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

######################### Disable Class For Testing Methods ####################
def send_login_otp(mobile_number, otp):
        print(mobile_number, otp, "LOgin OTP")
        # template_id = "624d33cb9297f627a65d815a"
        # auth_key = "331717AW6OVIv5HJE5eddebabP1"
        # conn = http.client.HTTPSConnection("api.msg91.com")
        # headers = { 'Content-Type': "application/json" }
        # payload = "{\"Value1\":\"Param1\",\"Value2\":\"Param2\",\"Value3\":\"Param3\"}"
        # # /api/v5/otp?template_id=&mobile=&authkey="
        # # url = "/api/v5/otp?template_id="+template_id+"&mobile="+mobile_number+"&authkey="+auth_key
        # url = "/api/v5/otp?template_id=624d33cb9297f627a65d815a&mobile=919913887143&authkey=331717AW6OVIv5HJE5eddebabP1"
        # print(url)
        # conn.request("GET", url, headers)

        # res = conn.getresponse()
        # data = res.read()

        # print(data.decode("utf-8"))

class LoginView(View):
    form_class = LoginFormView
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        message = ''
        form = self.form_class()
        return render(request, self.template_name, context={'form':form, 'message': message})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        mobile_number = request.POST.get('mobile_number')
        print(mobile_number)
        
        # try:
        custom_user = CustomUser.objects.filter(mobile_number=mobile_number).first()
        if custom_user:
            otp = str(random.randint(100000, 999999))
            print(otp, "otp when generated")
            custom_user.otp = otp
            custom_user.save()
            send_login_otp(mobile_number, otp)
            request.session['mobile_number'] = mobile_number
            return redirect('otp')
        else:
            messages.error(request, "Mobile Number Not Registered")
            return render(request, self.template_name, context={'form':form, 'messsage':message})
        # except:
        #     raise ValidationError("Mobile Number Not Registered") 
        # message.error(request, "Mobile Number Not Registered")
    
    # success_url = 'otp'

class OTPView(View):
    form_class = OTPForm
    template_name = 'login/otp.html'

    def get(self, request, *args, **kwargs):
        message = ''
        form = self.form_class()
        return render(request, 'login/otp.html', context={'form':form, 'message': message})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        mobile_number = request.session.get('mobile_number')
        otp = request.POST.get('otp')
        user = authenticate(mobile_number=mobile_number, otp=otp)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/blog/list/')
        else:
            return redirect('login')

class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)