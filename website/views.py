from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as user_login
from website.models import myuploadfiles

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    if request.method =="POST":
        myfile = request.FILES.getlist("uploadfiles")        
        for f in myfile:
            myuploadfiles(myfiles=f).save()
            messages.success(request,"Your File uploaded Sucessfully")
        return render(request,'sigout.html')
    return render(request,'index.html') 

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['psw']
        password2 = request.POST['psw2']

        if User.objects.filter(email=email):
            messages.error(request,"Email Alreay Exist !")
            return redirect('signup')    

        if User.objects.filter(username=username ):
            messages.error(request,"Username already Exist! please try some other Username ")
            return redirect('signup')

        if password != password2:
            messages.error(request,"Passwords didn't match !")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request,"Username must be AlphaNumeric !")            
            return render('signup')

        myuser = User.objects.create_user(username,email,password)
        myuser.pass2 = password2
        myuser.save()
        messages.success(request,"Your Account is Sucessfully Register ")
        return redirect('login')
    return render(request,'signup.html')


def login(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password )
        if user is not None:
            user_login(request,user)
            messages.success(request,"Login SucessFull")
            return redirect('index')
        else:            
            messages.error(request,"Bad Credintioals")
        return redirect('login')
    return render(request,'login.html')

