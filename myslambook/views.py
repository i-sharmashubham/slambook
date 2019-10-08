from django.shortcuts import render,redirect
from django.http import Http404
from .models import Slam
from .forms import SlamBook,Register,Login
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.admin import User
from django.contrib.staticfiles.templatetags.staticfiles import static

def index(request):
    return render(request, 'myslambook/index.html')

def dashboard(request):
    if request.user.is_authenticated:
        all_slam = Slam.objects.filter(user=request.user.username)
        if request.user.is_superuser:
            all_slam = Slam.objects.all()
        return render(request, 'myslambook/dashboard.html', {'all_slam' : all_slam})
    return redirect('/myslambook/userlogin')

def details(request,slam_id):
    if request.user.is_authenticated:
        try:
            slam = Slam.objects.get(id=slam_id)
            if slam.user != request.user.get_username():
                if not request.user.is_superuser:
                    raise Http404("Data does't exist")
        except Slam.DoesNotExist:
            raise Http404("Data does't exist")
        return render(request, 'myslambook/details.html', {'slam' : slam})
    return redirect('/myslambook/userlogin')

def addnewslam(request,user_id):
    try:
        u = User.objects.get(username=str(user_id))
        un = u.first_name + ' ' + u.last_name
    except Users.DoesNotExist:
        raise Http404("Data does't exist")
    if request.method == 'GET':
        form = SlamBook(None)
        return render(request, 'myslambook/addnewslam.html', {'name' : un, 'username' : u.username, 'form':form})

    if request.method == 'POST':
        form = SlamBook(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'myslambook/addslam.html', {'name' : request.POST['name']})
        return render(request, 'myslambook/addnewslam.html', {'name' : un,'username':user_id, 'form':form})
    raise Http404("Data does't exist")
        

def delete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id=request.POST['id']
            Slam.objects.filter(id=id).delete()
            return redirect('/myslambook/dashboard')
        raise Http404("Data does't exist")
    return redirect('/myslambook/userlogin')


def register(request):
    if request.user.is_authenticated:
        return redirect('/myslambook/dashboard')
    if request.method == 'GET':
        form = Register(None)
        return render(request, 'myslambook/register.html', {'form' : form})

    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myslambook/userlogin')
        return render(request, 'myslambook/register.html', {'form' : form})

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('/myslambook/dashboard')

    if request.method == 'GET':
        form = Login(None)
        return render(request, 'myslambook/login.html', {'form' : form})

    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/myslambook/dashboard')
            else:
                form.errors.password = 'Invalid username or password'
                return render(request, 'myslambook/login.html', {'form' : form})
        return render(request, 'myslambook/login.html', {'form' : form})

def userlogout(request):
    logout(request)
    return redirect('/myslambook')


def share(request):
    if request.user.is_authenticated:
        prefix = 'https://' if request.is_secure() else 'http://'
        url = prefix + str(request.get_host()) + '/myslambook/addnewslam/' + request.user.get_username()
        return render(request, 'myslambook/share.html',{'url':url})
    return redirect('/myslambook/userlogin')


def birthdays(request):
    if request.user.is_authenticated:
        month = ['January','Fabruary','March','April','May','June','July','August','September','October','November','December']
        all_slam = Slam.objects.filter(user=request.user.username)
        if request.user.is_superuser:
            all_slam = Slam.objects.all()
        return render(request, 'myslambook/birthdays.html', {'all_slam' : all_slam, 'month':month})
    return redirect('/myslambook/userlogin')


def demo(request):
    all_slam = Slam.objects.all()
    return render(request, 'myslambook/demo.html',{'slam':all_slam})





    
    