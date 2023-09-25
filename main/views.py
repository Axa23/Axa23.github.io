# main/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def trainers(request):
    return render(request, "trainers.html")

def events(request):
    return render(request, "events.html")

def pricing(request):
    return render (request,"pricing.html")

def contact(request):
    return render(request,'contact.html')

def coursedetails(request):
    return render(request, "course-details.html")

def formcontact(request):
    return render(request, "contact.php")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('courses')  # Redirect to the courses page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def base(request):
    return render(request, 'base.html')


    

# ... And so on for each template


# Create your views here.
