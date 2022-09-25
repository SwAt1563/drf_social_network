from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import json
# Create your views here.


def home(request):
    return render(request, 'home/home.html', {'slug': 'qutaiba-olayyan'})



# update the value of the token
# or put it null
def store_token(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            request.session['access'] = data.get('access')
            request.session['refresh'] = data.get('refresh')
        else:
            request.session['access'] = None
            request.session['refresh'] = None
    return HttpResponse('Token saved')
