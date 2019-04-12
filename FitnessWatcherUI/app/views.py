import requests
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from app.forms import ProfileForm, UserForm

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def loginview(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'app/login.html')
    else:
        user_form = UserForm()
    return render(request, 'app/login.html')

def register(request):
    if request.method=='POST':
        profile_form = ProfileForm(request.POST,prefix='Profile')
        user_form = UserForm(request.POST, prefix='User')
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            password = request.POST['User-password']
            user.set_password(password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return HttpResponseRedirect('/')
    else:
        profile_form = ProfileForm(prefix='Profile')
        user_form = UserForm(prefix='User')
    return render(request, 'app/register.html', {'profile_form': profile_form, 'user_form': user_form})

def GetBlogs(request):
    response = requests.get('http://localhost:8001/api/v2/blogs?format=json')
    if response.status_code == 200:
        _blogs = response.json()
    print(_blogs)
    return render(request, 'app/blogs.html', context={'blogs': _blogs})