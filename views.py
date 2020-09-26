from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail

from s_project import settings
from django.conf import settings


def home(request):
  return render(request,'home.html')

def add(request) :
  val1 = int(request.POST["num1"])
  val2 = int(request.POST["num2"])
  Output= val1+val2
  return render(request, "Result.html", {'result':Output})

def multiply(request) :
  val1 = int(request.POST["num1"])
  val2 = int(request.POST["num2"])
  Mult_Output= val1*val2
  return render(request, "Result.html", {'result':Mult_Output})

def test_page(request):
  return HttpResponse('teeee')

def wish(request):
  return HttpResponse('Hi, Good Morning')

def signup(request):
  if request.method == 'POST':

    username=request.POST['username']
    first_name= request.POST['name1']
    name2 = request.POST['name2']
    Email_ID = request.POST['e_mail']
    pw = request.POST['pw']
    x=User.objects.create_user(username = username, first_name= first_name,
                               last_name =name2,
                               email= Email_ID,
                               password= pw)
    x.save()
    subject = 'Verify your Email'
    message = 'Hello' + x.first_name + 'This is a verification Email'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [x.email]
    send_mail(subject, message, email_from, recipient_list)
    print("user_created")
    return redirect ('/')
  else :
    return render(request, 'Signup.html',{'signup2':'http://127.0.0.1:8000/signup'})

def email_confirmation(request):
  subject = 'Hello God'
  message = 'Hi, this is a test mail'
  email_from = settings.EMAIL_HOST_USER
  recipient_list = ['ananthesh.adiga@gmail.com','abhiramvasistacv@gmail.com']
  send_mail(subject,message,email_from,recipient_list)
  return HttpResponse('email test')


