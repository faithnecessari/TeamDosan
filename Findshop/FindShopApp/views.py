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
            messages.info(request,'Password and Repassword are not the same!')
            # return redirect("register")

        elif customer.CustomerId=="" or customer.Fname=="" or customer.Lname=="" or customer.ContactNum=="" or customer.Street=="" or customer.City_Municipality=="" or customer.Province=="" or customer.Username=="":
            messages.info(request,'Some Fields are Empty')
            # return redirect("register")

        else:
            customer.save()
            messages.info(request, 'Successfully Registered!')
            # return render(request,'login.html')
       
    return render(request,'register.html')

class MyDashboardCustomerView(View):
    def get(self, request):
        customers = Customer.objects.all()
        context = {
            'customer': customers
        }

        return render(request,'dashboardCustomer.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                id = request.POST.get("id")
                Fname = request.POST.get("Fname")
                Lname = request.POST.get("Lname")
                ContactNum = request.POST.get("ContactNum")
                Street = request.POST.get("Street")
                City_Municipality = request.POST.get("City_Municipality")
                Province = request.POST.get("Province")
                
                update = Customer.objects.filter(id = id).update(id = id, Fname = Fname, Lname = Lname, ContactNum = ContactNum, Street = Street, City_Municipality=City_Municipality,Province=Province)
                print(update)
                print('profile updated')
                messages.info(request,"Successfully Updated!")
                return redirect('my_dashboard_customer_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                delete = Customer.objects.filter(id=id).delete()
                # pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
                messages.info(request,"Successfully Deleted!")
                
                #return HttpResponse ('post')
                return redirect('my_dashboard_customer_view')
            
class MyDashboardAdminView(View):
    def get(self, request):
        admin = Admin.objects.all()
        context = {
            'admins': admin
        } 
        return render(request,'dashboardAdmin.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                id = request.POST.get("id")
                Fname = request.POST.get("Fname")
                Lname = request.POST.get("Lname")
                Username = request.POST.get("Username")
                Password = request.POST.get("Password")
                
                update_admin = Admin.objects.filter(id = id).update(Fname = Fname, Lname = Lname, Username = Username, Password = Password)
                print(update_admin)
                print('profile updated')
                return redirect('my_dashboard_admin_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                admindel = Admin.objects.filter(id=id).delete()
                print('recorded deleted')
                return redirect('my_dashboard_admin_view')

class MyAdminDashboardCustomerView(View):
    def get(self, request):
        customers = Customer.objects.all()
        context = {
            'customer': customers
        }

        return render(request,'AdmindashboardCustomer.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                id = request.POST.get("id")
                Fname = request.POST.get("Fname")
                Lname = request.POST.get("Lname")
                ContactNum = request.POST.get("ContactNum")
                Street = request.POST.get("Street")
                City_Municipality = request.POST.get("City_Municipality")
                Province = request.POST.get("Province")
                
                update_book = Customer.objects.filter(id = id).update(id = id, Fname = Fname, Lname = Lname, ContactNum = ContactNum, Street = Street, City_Municipality=City_Municipality,Province=Province)
                print(update_book)
                print('profile updated')
                return redirect('my_dashboard_customer_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                bookdel = Customer.objects.filter(id=id).delete()
                # pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
                #return HttpResponse ('post')
                return redirect('my_dashboard_customer_view')
            
 class dashboardView(View):
    def get(self, request):
        reservation = Reservation.objects.all()
        return render(request, 'dashboard.html',{"reservation" : reservation})

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                id = request.POST.get("id")
                date = request.POST.get("date")
                time = request.POST.get("time")
                product = request.POST.get("product")
                
                update = Reservation.objects.filter(id = id).update(date = date, time = time, product = product)
                print(update)
                print('profile updated')
                return redirect('dashboard_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                delete = Reservation.objects.filter(id=id).delete()
                # pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
                #return HttpResponse ('post')
                return redirect('dashboard_view')
            
class reservationView(View):
    def get(self,request):
        return render(request,'reservation.html' , {})

    def post(self, request):
        form = ReservationForm(request.POST)
        
        if form.is_valid():
            id = request.POST.get("id")
            date = request.POST.get("date")
            time = request.POST.get("time")
            product = request.POST.get("product")

            form = Reservation(id = id, date = date, time = time, product = product)
            form.save()
            
            return redirect('dashboard_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')

class MyDashboardMainView(View):
    def get(self, request):

        return render(request,'dashboardmain.html')

class MyProductRegistrationView(View):
    def get(self, request):

        return render(request,'registration.html') 

    def post(self, request):
        form = ProductsForm(request.POST)

        if form.is_valid():
            shopID = request.POST.get("shopID")         
            productName = request.POST.get("productName")
            quantity = request.POST.get("quantity")
            price = request.POST.get("price")
            
            form = Products(productName=productName, quantity=quantity, price=price, shopID_id = shopID)
            form.save()

            return redirect('my_dashboard_main_view')
        
        else:
            print(form.errors)
        return HttpResponse('not valid')

class MyDashboardView(View):
    def get(self, request):
        product = Products.objects.all()
        shop = Shops.objects.all()

        return render(request,'dashboardProd.html',{"product" : product, "shop": shop})
    def post(self, request):
            if request.method == 'POST':
                if 'btnUpdate' in request.POST: 
                    print('update profile button clicked')
                    pid= request.POST.get("product-id")
                    productName = request.POST.get("productName")
                    quantity = request.POST.get("quantity")
                    price = request.POST.get("price")
                    shopID= request.POST.get("shopID")
                    update_product = Products.objects.filter(id = pid).update(productName = productName, quantity = quantity, price = price, shopID_id = shopID)
                    print(update_product)
                    print('profile updated')
                    return redirect('my_dashboard_view')
                elif 'btnDelete' in request.POST:
                    print('delete button clicked')
                    id = request.POST.get("pid")
                    productdel = Products.objects.filter(id=id).delete()
                    # pers = Person.objects.filter(id = sid).delete()
                    print('recorded deleted')
                    #return HttpResponse ('post')
            return redirect('my_dashboard_view')
        
class MyDashboardReservationView(View):
    def get(self, request):
        reservation = Reservation.objects.all()

        return render(request,'dashboardReservation.html',{"reservation" : reservation})
        
    def post(self, request):
            if request.method == 'POST':
                if 'btnUpdate' in request.POST: 
                    print('update profile button clicked')
                    id= request.POST.get("id")
                    Fname = request.POST.get("Fname")
                    Lname = request.POST.get("Lname")
                    Product = request.POST.get("Product")
                    Date= request.POST.get("Date")
                    Time= request.POST.get("Time")
                    Status = request.POST.get("Status")
                    update_reservation = Reservation.objects.filter(id = id).update(Fname = Fname, Lname = Lname, Product = Product, Date = Date, Time = Time, Status = Status)
                    print(update_reservation)
                    print('profile updated')
                    return redirect('my_dashboard_reservation_view')
           
                elif 'btnDelete' in request.POST:
                    print('delete button clicked')
                    id = request.POST.get("id")
                    reservedel = Reservation.objects.filter(id=id).delete()
                    # pers = Person.objects.filter(id = sid).delete()
                    print('record deleted')
                    #return HttpResponse ('post')
                    return redirect('my_dashboard_reservation_view')
            
class productView(View):
    def get(self, request):
        return render(request,'product.html' , {})
     
class shopView(View):
    def get(self, request):
        shop = Shops.objects.all()
        return render(request,'shop.html' ,{"shops" : shop})

    def post(self, request):
        
        if request.method == 'POST':
                productid = request.POST.get("productID")
                shopName = request.POST.get("shopname")
                #street = request.POST.get("street")
                #cityMunicipality = request.POST.get("citymunicipality")
                #province = request.POST.get("province")
                
                viewShops =  Shops.objects.filter(productID= productid).Select(shopname = shopName)
                print(viewShops)
                return redirect('reservation_view')
           
            
