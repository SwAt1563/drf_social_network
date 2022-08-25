from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.


def post(request):
    return render(request, 'post/post.html')

def edit_post(request):
    return render(request, 'post/edit_post.html')