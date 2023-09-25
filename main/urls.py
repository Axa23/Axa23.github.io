"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('courses.html',views.courses, name='courses'),
    path('trainers.html',views.trainers, name='trainers'),
    path('events.html',views.events, name='events'),
    path('pricing.html',views.pricing, name='pricing'),
    path('contact.html',views.contact, name='contact'),
    path('course-details.html',views.coursedetails,name='coursedetails'),
    path('contact.php',views.formcontact,name='formcontact'),
    path('login.html', views.login_view, name='login'),
    # ... And so on for each view
]



