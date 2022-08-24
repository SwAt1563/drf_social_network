from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request, 'user_profile/profile.html')

def edit_profile(request):
    return render(request, 'user_profile/edit.html')