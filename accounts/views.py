from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def register(request):
     if request.method == 'POST':
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          username = request.POST['username']
          email = request.POST['email']
          password1 = request.POST['password1']
          password2 = request.POST['password2']
          
          if password1==password2:
               if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already taken!')
                    return redirect('/accounts/register/')
               elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already exists')
                    return redirect('/accounts/register/')
               else:
                    newuser = User(first_name=first_name,last_name=last_name,username=username,email=email)
                    newuser.set_password(password1)
                    newuser.save()
                    print('user created!')
          else:
               messages.info(request,'Password mismatch!')
               return redirect('/accounts/register/')
          
          return redirect('/')
          
          
     else:
          return render(request,'register.html')
          
def login(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          
          user = auth.authenticate(username=username, password=password)
          
          if user is not None:
               auth.login(request,user)
               return redirect('/')
          else:
               messages.info(request,'Invalid credentials!'+str(username)+str(password)+str(user))
               return redirect('/accounts/login/')
     else:
          return render(request,'login.html')
          
def logout(request):
     auth.logout(request)
     return redirect('/')