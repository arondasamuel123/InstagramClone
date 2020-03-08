from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from .forms import SignUpForm,LoginForm
from .token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from .email import activation_email
from django.contrib.auth import login, authenticate, logout
def home(request):
    
    return render(request,'home.html')
    
def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            to_email = form.cleaned_data.get('email')
            activation_email(user, current_site, to_email)
            return HttpResponse('Check your email to verify your account')
    else:
        form = SignUpForm()
    return render(request, 'django_registration/registration_form.html', {"form":form})


def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request,user)
            return render(request, 'home.html')
        else:
            HttpResponse("Activation link is invalid")
def login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            
            user = authenticate(username,password)
            if user.is_active:
                login(request,user)
                return redirect(home)
            else:
                return HttpResponse("Your account is inactive")
            
    else:
        form=LoginForm()
    return render(request, 'registration/login.html',{"form":form})

def logout_view(request):
    logout(request)
    
    return redirect(home)
        
        
        
    