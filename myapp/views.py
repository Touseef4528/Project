from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from myapp.models import login_user, registration_user

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        if registration_user.objects.filter(email=email).exists():
            if registration_user.objects.filter(email=email, password=password):

                    request.session['var'] = email
                    request.session.save()
                    return render(request, 'index.html')

            else:
                messages.warning(
                    request, 'Your E-mail or Password is Incorrect...!!!')

        else:
                messages.warning(
                    request, 'You are not a Registered User, Register First...!!!')

        print(email, password)
        return render(request, 'login.html')
    return render(request, 'login.html')


def register(request):

    if request.method == 'POST':

        name = request.POST.get('regname')
        email = request.POST.get('regemail')
        password = request.POST.get('regpassword')

        regdata = registration_user(name=name, email=email, password=password)
        regdata.save()
        messages.warning(
            request, 'You are Registered Successfully, Now Login Again...!!!')

        print(name, email, password)

        return render(request, 'registration.html')

    return render(request, 'registration.html')


def logout(request):

    request.session.flush()
    request.session.clear_expired()

    messages.warning(
        request, 'You are Logged Out Now, You must have To Login again 😊😊😊')

    return render(request, 'login.html')

def new(request):
    return render(request, 'new.html')

def getsession(request):
     
        if 'var' in request.session:
            name = request.session['var']
            return render(request, 'getsession.html', {'name': name})

        else:
            messages.warning(
                request, 'You are Logged Out Now, You must have To Login again 😊😊😊')

        return render(request, 'getsession.html')
