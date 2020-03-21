# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User,auth


# # Create your views here.

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             return redirect('/')
#         else:
#             return redirect('/account/login')
#     else:
#         return render(request,'login.html',)


# def logout(request):
#     auth.logout(request)
#     return redirect('/')

# def signup(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password_1 = request.POST['password_1']
#         password_2 = request.POST['password_2']
#         if first_name and last_name and username and email and password_1 and password_2:
#             if password_1 == password_2:
#                 user = User.objects.create_user(first_name=first_name,last_name=last_name,
#                                                username=username,email=email,password=password_2 )
#                 user.save()
#                 return redirect('/')
#             else:
#                 return redirect('/account/signup')
#         else:
#             return redirect('/account/signup')

#     else:
#         return render(request,'signup.html',)

from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method=='POST':
        if request.POST['username'] and request.POST['password']:
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                return redirect('/account/login')
        else:
             return redirect('/account/login')       
    else:
        return render(request,'login.html',)

def logout(request):
    auth.logout(request)
    return redirect('/')
    # return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username=request.POST['username']
        email= request.POST['email']
        password_1=request.POST['password_1']
        password_2=request.POST['password_2']
        if first_name and last_name and username and email and password_1 and password_2:
            if password_1==password_2:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password_2)
                user.save()
                return redirect('/')
            else:
                return redirect('/account/signup')
        else:
            return redirect('/account/signup')
    else:
        return render(request,'signup.html',)