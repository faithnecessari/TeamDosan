from django.http import Http404
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
import mysql.connector
from django.contrib import messages
from .forms import *
from .models import *
from FindShopApp.models import Customer
from operator import itemgetter

# Create your views here.
class MyIndexView(View):
    def get(self, request):

        return render(request,'index.html')

class MyIndexViewCustomer(View):
    def get(self, request):

        return render(request,'index Customer.html')

class MySigninView(View):
    def get(self, request):

        return render(request,'signinBoard.html')


class MyLandingView(View):
    def get(self, request):

        return render(request,'landing.html')

class MyAdminRegistrationView(View):
    
    def get(self, request):

        return render(request,'registrationAdmin.html')

    def post(self, request):
        form = AdminForm(request.POST)

        if form.is_valid():
            AdminId = request.POST.get("id")
            Fname = request.POST.get("Fname")           
            Lname = request.POST.get("Lname")
            Username = request.POST.get("Username")
            Password = request.POST.get("Password")
            
            form = Admin(id=AdminId,Fname=Fname, Lname=Lname, Username=Username, Password=Password)
            form.save()

            return redirect('my_landing_view')
        
        else:
            print(form.errors)
        return HttpResponse('not valid')
        

class MyCustomerRegistrationView(View):
    def get(self, request):
        return render(request,'registrationCustomer.html')

    def post(self, request):
        form = CustomerForm(request.POST)

        if form.is_valid():
            # CostumerId = request.POST.get("CostumerId")
            Fname = request.POST.get("Fname")         
            Lname = request.POST.get("Lname")
            ContactNum = request.POST.get("ContactNum")
            Street = request.POST.get("Street")
            City_Municipality = request.POST.get("City_Municipality")
            Province = request.POST.get("Province")
            # Username = request.POST.get("Username")
            # Password = request.POST.get("Password")
            
            form = Customer( Fname=Fname, 
                Lname=Lname, 
                ContactNum=ContactNum, 
                Street=Street,
                City_Municipality=City_Municipality, 
                Province=Province)
            form.save()

            return redirect('my_dashboard_main_view')
        
        else:
            print(form.errors)
            return HttpResponse('not valid')

def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'authentication/login.html', context={'form': form})


def feedback(request):
    
        if request.method=='POST':
            contact=Contact()
            name=request.POST.get("name")
            email=request.POST.get("email")
            subject=request.POST.get("subject")
            contact.name=name
            contact.email=email
            contact.subject=subject
            contact.save()
            return HttpResponse("<h1>Thanks For Contacting Us!</h1>")
        return render(request,'feedback.html')


def login(request):
    con = mysql.connector.connect(host="localhost",user="root",passwd="", database="findshop")
    cursor=con.cursor()
    con2 = mysql.connector.connect(host="localhost",user="root",passwd="", database="findshop")
    cursor2=con2.cursor()
    sqlcommand="SELECT Username from findshopapp_customer"
    sqlcommand2="SELECT Password from findshopapp_customer"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    u=[]
    p=[]

    for i in cursor:
        u.append(i)

    for j in cursor2:
        p.append(j)

    res= list(map(itemgetter(0),u))
    res2= list(map(itemgetter(0),p))


    if request.method=="POST":
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        i=0
        k=len(res2)
        while i<k:
            if res[i]==Username and res2[i]==Password:
                return render(request,'index Customer.html',{'Username':Username})
                break
            i+=1
        else:
            messages.info(request,"*Check Username or Password*")
            # return redirect("login")
    

    return render(request,'login.html')

def loginAdmin(request):
    con = mysql.connector.connect(host="localhost",user="root",passwd="", database="findshop")
    cursor=con.cursor()
    con2 = mysql.connector.connect(host="localhost",user="root",passwd="", database="findshop")
    cursor2=con2.cursor()
    sqlcommand="SELECT Username from findshopapp_admin"
    sqlcommand2="SELECT Password from findshopapp_admin"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    u=[]
    p=[]

    for i in cursor:
        u.append(i)

    for j in cursor2:
        p.append(j)

    res= list(map(itemgetter(0),u))
    res2= list(map(itemgetter(0),p))


    if request.method=="POST":
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        i=0
        k=len(res2)
        while i<k:
            if res[i]==Username and res2[i]==Password:
                return render(request,'index.html',{'Username':Username})
                break
            i+=1
        else:
            messages.info(request,"*Check Username or Password*")
            # return redirect("login")
    

    return render(request,'login Admin.html')

def register(request):
    if request.method=="POST":
        customer=Customer()

        CustomerId = request .POST.get("CustomerId")
        Fname = request.POST.get("Fname")         
        Lname = request.POST.get("Lname")
        ContactNum = request.POST.get("ContactNum")
        Street = request.POST.get("Street")
        City_Municipality = request.POST.get("City_Municipality")
        Province = request.POST.get("Province")
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        repassword = request.POST.get("repassword")

        customer.CustomerId = CustomerId
        customer.Fname = Fname        
        customer.Lname = Lname
        customer.ContactNum = ContactNum
        customer.Street = Street
        customer.City_Municipality = City_Municipality
        customer.Province = Province
        customer.Username = Username
        customer.Password = Password
        customer.repassword = repassword
        
        if customer.Password != customer.repassword:
            messages.info(request,'*Password and Repassword are not the same!*')
            # return redirect("register")

        elif customer.CustomerId=="" or customer.Fname=="" or customer.Lname=="" or customer.ContactNum=="" or customer.Street=="" or customer.City_Municipality=="" or customer.Province=="" or customer.Username=="":
            messages.info(request,'*Some Fields are Empty*')
            # return redirect("register")

        else:
            customer.save()
            # return render(request,'login.html')
       
    return render(request,'register.html')