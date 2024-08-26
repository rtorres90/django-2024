from django.shortcuts import render

# Create your views here.

def user_create(request):
    return render(request, 'users/user_create.html', {'greetings': "Welcome to user creation page!"})