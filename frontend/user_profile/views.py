from django.shortcuts import render
from django.http import HttpResponse
from frontend.api import get_method, put_method
from django.forms import Form
import requests

# Create your views here.

def profile(request, slug):
    return render(request, 'user_profile/profile.html')

def edit_profile(request, slug):
    url = "user_profile/" + str(slug)
    if request.method == 'GET':
        response = get_method(request, url)
        if response:
            return render(request, 'user_profile/edit.html', {'slug': slug, 'response': response})
        return HttpResponse('Something went wrong')
    elif request.method == 'POST':
        form = request.POST
        data = {'name': form.get('name'), 'location': form.get('location')}
        response = put_method(request, url, data)
        return render(request, 'user_profile/edit.html', {'slug': slug, 'response': response})


