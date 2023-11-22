from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
import requests
from django.contrib.auth.models import User
from booking.models import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required , user_passes_test



def index(request):
    return render(request, 'index.html')


def menu_view(request):
    url = 'http://127.0.0.1:8000/api/menu-item'
    try:
        response = requests.get(url)

        if response.status_code == 200:
            menu_data = response.json()
            return render(request , 'menu.html', {'menu_items':menu_data})
        else:
            return HttpResponse("Error While Call Api")

    except requests.RequestException as e:
        return HttpResponse('Error {}'.format(e))       
    
def book(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            date = request.POST.get('date')
            time = request.POST.get('time')
            newBook = Reservation(name=name, date=date, time=time)
            newBook.save()
            return HttpResponse("Thanks")
        except:
            return render(request, "book.html", {'msg':"Already Booked"})

    return render(request, "book.html")


def getBook(request):
    date = request.GET.get('date')
    books = Reservation.objects.filter(date = date)
    selected_date = [{
        "name": book.name,
        "time":book.time
    }
    for book in books ]
    return JsonResponse(selected_date, safe=False)



def signup_view(request):
    if request.user.is_authenticated:
        logout(request)
    message = {'email':'Email is already exist', 'username':'username is already exist', 'valid':'Enter Valid Data'}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        if User.objects.filter(username=username).exists() == True:
            return render(request, 'register.html',{'message':message['username']})
        elif User.objects.filter(email=email).exists() == True:
            return render(request, 'register.html',{'message':message['email']})
        else:
            newUser = User.objects.create_user(username, email, password)
            newUser.save()
            return redirect('/login')
    return render(request, 'register.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    message = 'username or password is incorrect'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(username=username , password = password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request , 'login.html' , {'msg': 'Incorrect'})

    return render(request, 'login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('/')

