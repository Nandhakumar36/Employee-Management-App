from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('managersignup/', views.managersignup, name='managersignup'),
    path('managerlogin/', views.managerlogin, name='managerlogin'),
    path('managerdashboard/', views.managerdashboard, name='managerdashboard'),
    path('showmanagerdetails/', views.showmanagerdetails, name='showmanagerdetails'),
    path('empdashboard/', views.empdashboard, name='empdashboard'),
    path('manempcrud/', views.manempcrud, name='manempcrud'),
    path('Employeesignup/', views.Employeesignup, name='Employeesignup'),
    path('employeelogin/', views.employeelogin, name='employeelogin'),
    path('addmanemp/', views.addmanemp, name='addmanemp'),
    path('updatemanemp/', views.updatemanemp, name='updatemanemp'),
    path('deleteemp/', views.deleteemp, name='deleteemp'),
    path('deletemanemp/', views.deletemanemp, name='deletemanemp'),
    path('logout/', views.logout, name='logout'),
    
]
