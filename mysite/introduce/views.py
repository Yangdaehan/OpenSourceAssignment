from django.shortcuts import render

# Create your views here.
from .models import Friend
def index(request):
    friend_list = Friend.objects.all()
    context = {'friend_list': friend_list}

    return render(request, 'introduce/index.html',context)

def my_view(request):

    return render(request, 'introduce/friend_1.html')


def my_view_1(request):

    return render(request, 'introduce/friend_2.html')
