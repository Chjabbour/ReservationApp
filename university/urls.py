"""university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from student import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('studentdetails/', views.studentdetails, name='studentdetails'),
    path('bookdetails/', views.bookdetails, name='bookdetails'),
    path('login/', LoginView.as_view(template_name='student/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('comment/', views.commentpage, name='comment'),
    path('savecomment/', views.savecomment, name='savecomment'),
    path('reservation/', views.reserve, name='reserve'),
    path('chart/', views.chart, name='chart'),
    path('savereservation/', views.savereservation, name='savereservation'),
]
