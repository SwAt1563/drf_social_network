from django.shortcuts import render

# Create your views here.


def settings(request):
    return render(request, 'user_settings/settings.html')