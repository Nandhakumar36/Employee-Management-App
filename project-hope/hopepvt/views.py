from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Manager
import datetime
import random
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return render (request,'index.html')

def managersignup(request):
    if request.method == 'POST':
        manid= 'W2sm-'+str(datetime.date.today().strftime("%m%d"))+'-'+str(datetime.datetime.now().strftime("%H%M%S"))
        request.session['managername'] = request.POST['name']
        request.session['manageremail'] = request.POST['email']
        request.session['managermobile'] = request.POST['mobile']
        request.session['managerpassword'] = request.POST['password']
        request.session['confirm_password'] = request.POST['confirm_password']
        if request.POST['password'] == request.POST['confirm_password']:
            if Manager.objects.filter(email=request.POST['email']).exists():
                messages.info(request, "Email already used")
                return redirect('managersignup')
            else:
                newmanager = Manager(
                    firstname=request.session['managername'],email=request.session['manageremail'],
                    password=request.session['managerpassword'],mobile=request.session['managermobile'],mid=manid
                )
                newmanager.save()
                return redirect('/')
        else:
            messages.info(request, "password 1 and password 2 doesn't match")
            return redirect('managersignup')
    else:           
        return render (request,'managersignup.html')

def managerlogin(request):
    pop = 0
    if request.method == 'POST':
            try:
                user = Manager.objects.get(
                    email=request.POST['email'], password=request.POST['password'])
                request.session['managername'] = user.firstname
                request.session['manageremail'] = user.email
                request.session['managermobile'] = user.mobile
                request.session['mid'] = user.mid
                return redirect("managerdashboard")
            except:
                pop = 1
                context = {'pop': pop}
                return render(request, 'managerlogin.html', context)
    return render (request,'managerlogin.html')


def managerdashboard(request):
    context = {'name': request.session['managername'], 'mobile': request.session['managermobile'],
        'email': request.session['manageremail'] 
    }
    return render(request, 'managerdashboard.html', context)


def manempcrud(request):

    if request.method == 'POST':
        Emp = Employee.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(Emp, 30)
        try:
            Emp = paginator.page(page)
        except PageNotAnInteger:
            Emp = paginator.page(1)
        except EmptyPage:
            Emp = paginator.page(paginator.num_pages)
       
        context = {'name': request.session['managername'], 'Emp': Emp}
        return render(request, 'manempcrud.html', context)
    else:
        Emp = Employee.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(Emp, 30)
        try:
            Emp = paginator.page(page)
        except PageNotAnInteger:
            Emp = paginator.page(1)
        except EmptyPage:
            Emp = paginator.page(paginator.num_pages)
       
        context = {'name': request.session['managername'], 'Emp': Emp}
        return render(request, 'manempcrud.html', context)

def showmanagerdetails(request):
    manager = Manager.objects.get(email=request.session['manageremail'])
    context = {'name': request.session['managername'], 'manager': manager}
    return render(request, 'showmanagerdetails.html', context)
   

def Employeesignup(request):
    if request.method == 'POST':
        empid= 'W2se-'+str(datetime.date.today().strftime("%m%d"))+'-'+str(datetime.datetime.now().strftime("%H%M%S"))
        request.session['empname'] = request.POST['name']
        request.session['empemail'] = request.POST['email']
        request.session['empmobile'] = request.POST['mobile']
        request.session['emppassword'] = request.POST['password']
        request.session['empconfirm_password'] = request.POST['confirm_password']
        if request.POST['password'] == request.POST['confirm_password']:
            if Employee.objects.filter(email=request.POST['email']).exists():
                messages.info(request, "Email already used")
                return redirect('Employeesignup')
            else:
                newmanager = Employee(
                    firstname=request.session['empname'],email=request.session['empemail'],
                    password=request.session['emppassword'],mobile=request.session['empmobile'],eid=empid
                )
                newmanager.save()
                return redirect('/')
        else:
            messages.info(request, "password 1 and password 2 doesn't match")
            return redirect('Employeesignup')
    else:           
        return render (request,'Employeesignup.html')
    
def employeelogin(request):
    pop = 0
    if request.method == 'POST':
        try:
            empuser = Employee.objects.get(
                email=request.POST['email'], password=request.POST['password'])
            request.session['empname'] = empuser.firstname
            request.session['empemail'] = empuser.email
            request.session['empmobile'] = empuser.mobile
            request.session['eid'] = empuser.eid
            return redirect("empdashboard")
        except:
            pop = 1
            context = {'pop': pop}
            return render(request, 'employeelogin.html', context)
    return render (request,'employeelogin.html')
   
def addmanemp(request):
    if request.method == 'POST':
        empid= 'W2se-'+str(datetime.date.today().strftime("%m%d"))+'-'+str(datetime.datetime.now().strftime("%H%M%S"))
        request.session['empname'] = request.POST['name']
        request.session['empemail'] = request.POST['email']
        request.session['empmobile'] = request.POST['mobile']
        request.session['emppassword'] = request.POST['password']
        request.session['skill1'] = request.POST['Skill1']
        request.session['skill2'] = request.POST['Skill2']
        request.session['skill3'] = request.POST['Skill3']
        request.session['skill4'] = request.POST['Skill4']
        request.session['skill5'] = request.POST['skill5']
        request.session['percentage1'] = request.POST['percentage1']
        request.session['percentage2'] = request.POST['percentage2']
        request.session['percentage3'] = request.POST['percentage3']
        request.session['percentage4'] = request.POST['percentage4']
        request.session['percentage5'] = request.POST['percentage5']
        newemp = Employee(
            firstname=request.session['empname'],email=request.session['empemail'],
            password=request.session['emppassword'],mobile=request.session['empmobile'],eid=empid,skill1=request.session['skill1'],
            skill2=request.session['skill2'],skill3=request.session['skill3'],skill4=request.session['skill4'],
            skilll5=request.session['skill5'],
            skillpercentage1=request.session['percentage1'],skillpercentage2=request.session['percentage2'],
            skillpercentage3=request.session['percentage3'],skillpercentage4=request.session['percentage4'],
            skillpercentage5=request.session['percentage5']
        )
        newemp.save()
        return redirect('manempcrud')
    else:   
        context = {'name': request.session['managername']}        
        return render (request,'addmanemp.html',context)

def updatemanemp(request):
    if request.method == 'POST':
        if 'paybtn' in request.POST:
            emp = Employee.objects.get(id = request.POST['paybtn'])
            context = {'name': request.session['managername'],'emp':emp}        
            return render (request,'updatemanemp.html',context)
        elif 'upadteemp' in request.POST:
            request.session['empname'] = request.POST['name']
            request.session['empemail'] = request.POST['email']
            request.session['empmobile'] = request.POST['mobile']
            request.session['emppassword'] = request.POST['password']
            request.session['skill1'] = request.POST['Skill1']
            request.session['skill2'] = request.POST['Skill2']
            request.session['skill3'] = request.POST['Skill3']
            request.session['skill4'] = request.POST['Skill4']
            request.session['skill5'] = request.POST['skill5']
            request.session['percentage1'] = request.POST['percentage1']
            request.session['percentage2'] = request.POST['percentage2']
            request.session['percentage3'] = request.POST['percentage3']
            request.session['percentage4'] = request.POST['percentage4']
            request.session['percentage5'] = request.POST['percentage5']
            request.session['empid'] = request.POST['empid']

            Employee.objects.filter(id=request.POST['upadteemp']).update(
                firstname=request.session['empname'],email=request.session['empemail'],
                password=request.session['emppassword'],mobile=request.session['empmobile'],eid=request.session['empid'],
                skill1=request.session['skill1'],
                skill2=request.session['skill2'],skill3=request.session['skill3'],skill4=request.session['skill4'],
                skilll5=request.session['skill5'],
                skillpercentage1=request.session['percentage1'],skillpercentage2=request.session['percentage2'],
                skillpercentage3=request.session['percentage3'],skillpercentage4=request.session['percentage4'],
                skillpercentage5=request.session['percentage5']
            )
        
            return redirect('manempcrud')
        
    else:   
        context = {'name': request.session['managername']}        
        return render (request,'manempcrud.html',context)

def deletemanemp(request):
    if request.method == 'POST':
        if 'deleteemp' in request.POST:
            try:
                Employee.objects.filter(id = request.POST['deleteemp'] ).delete()
                return redirect('manempcrud')
            except:
                return redirect('manempcrud')
        else:
            return redirect('manempcrud')
    return redirect('manempcrud')

def empdashboard(request):
    if request.method == 'POST':
        request.session['skill1'] = request.POST['Skill1']
        request.session['skill2'] = request.POST['Skill2']
        request.session['skill3'] = request.POST['Skill3']
        request.session['skill4'] = request.POST['Skill4']
        request.session['skill5'] = request.POST['Skill5']
        request.session['percentage1'] = request.POST['Percentage1']
        request.session['percentage2'] = request.POST['Percentage2']
        request.session['percentage3'] = request.POST['Percentage3']
        request.session['percentage4'] = request.POST['Percentage4']
        request.session['percentage5'] = request.POST['Percentage5']
        Employee.objects.filter(email=request.session['empemail']).update(
            skill1=request.session['skill1'],
            skill2=request.session['skill2'],skill3=request.session['skill3'],skill4=request.session['skill4'],
            skilll5=request.session['skill5'],
            skillpercentage1=request.session['percentage1'],skillpercentage2=request.session['percentage2'],
            skillpercentage3=request.session['percentage3'],skillpercentage4=request.session['percentage4'],
            skillpercentage5=request.session['percentage5']
        )
    
        return redirect('empdashboard')

    else:
        emp = Employee.objects.get(email=request.session['empemail'])
        context = {'name': request.session['empname'], 'mobile': request.session['empmobile'],
            'email': request.session['empemail'] ,'emp':emp
        }
        return render(request, 'empdashboard.html', context)
def deleteemp(request):
    if request.method == 'POST':
        Employee.objects.filter(email=request.session['empemail']).delete()
        return redirect('empdashboard')

def logout(request):
    request.session.flush()
    return redirect('index')
