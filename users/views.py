from django.shortcuts import render,redirect
from .forms import SignUpForm,UpdateProfileForm
from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import CustomUser
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SignUpView(View):
    def get(self, request):
        return render(request, 'registration/signup.html', {'form': SignUpForm}) 
    
    def post(self, request):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is successfully created.')
            return redirect('login')
        return render(request, 'registration/signup.html', {'form': form})
    

class ProfileView(View, LoginRequiredMixin):
    login_url = 'login'
    def get(self, request,username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'profile.html', {'customuser': user})
    
class UpdateProfileView(View,LoginRequiredMixin):
    login_url = 'login'

    def get(self, request,username):
        user = get_object_or_404(CustomUser, username=username)
        form = UpdateProfileForm(instance=user)
        return render(request, 'profile_update.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, username=self.kwargs['username'])
        form = UpdateProfileForm(instance=user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is successfully updated.')
            return redirect('users:profile',user)
        return render(request, 'registration/signup.html', {'form': form})
    
def LogoutView(request):
    logout(request)
    return redirect('login')