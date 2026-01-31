from django.shortcuts import render
from .models import UserLogin, employee_details, shop_details, complaints, servicedetails, incharge_details, Food_store, Register

# Create your views here.

def showindex(request):
    return render(request, "index.html")


def admin_home(request):
    return render(request, "admin_home.html")

def user_home(request):
    return render(request, "user_home.html")

# UserLogin functions
def logcheck(request):
    if request.method == "POST":
        uname = request.POST.get('t1', '')
        request.session['username'] = uname
        pwd = request.POST.get('t2', '')
        checklogin = UserLogin.objects.filter(username=uname).values()
        for a in checklogin:
            utype = a['utype']
            upass = a['password']
            if (upass == pwd):
                if (utype == "admin"):
                    return render(request, 'admin_home.html')
                if (utype == "user"):
                    return render(request, 'user_home.html')
                else:
                    return render(request, 'login.html', context={'msg': 'check username or password'})
    return render(request, 'login.html')

def changepass(request):
    if request.method == 'POST':
        uname = request.session['username']
        currentpass = request.POST.get('t1', '')
        newpass = request.POST.get('t2', '')
        confirmpass = request.POST.get('t3', '')

        ucheck = UserLogin.objects.filter(username=uname).values()
        for a in ucheck:
            u = a['username']
            p = a['password']
            if u == uname and currentpass == p:
                if newpass == confirmpass:
                    UserLogin.objects.filter(username=uname).update(password=newpass)
                else:
                    return render(request, 'changepassword.html',{'msg': 'both the username and password are incorrect'})
            else:
                return render(request, 'changepassword.html',{'msg': 'invalid username'})
    return render(request, 'changepassword.html')


# Employee Details functions
def insertemployee_details(request):
    if request.method == "POST":
        employee_id = request.POST.get('t1')
        name = request.POST.get('t2')
        aadhar_no = request.POST.get('t3')
        email_id = request.POST.get('t4')
        date_join = request.POST.get('t5')
        work_type = request.POST.get('t6')
        mobile_no = request.POST.get('t7')
        employee_details.objects.create(
            employee_id=employee_id, name=name, aadhar_no=aadhar_no,
            email_id=email_id, date_join=date_join, work_type=work_type,
            mobile_no=mobile_no
        )
        return render(request, 'insertemployee_details.html')
    return render(request, 'insertemployee_details.html')

def employee_detailsview(request):
    userdict = employee_details.objects.all()
    return render(request, 'employee_detailsview.html', {'userdict': userdict})


# Shop Details functions
def insertshop_details(request):
    if request.method == "POST":
        shop_id = request.POST.get('t1')
        shop_type = request.POST.get('t2')
        owner_name = request.POST.get('t3')
        details = request.POST.get('t4')
        contact_no = request.POST.get('t5')
        shop_details.objects.create(
            shop_id=shop_id, shop_type=shop_type, owner_name=owner_name,
            details=details, contact_no=contact_no
        )
        return render(request, 'insertshop_details.html')
    return render(request, 'insertshop_details.html')

def shop_detailsview(request):
    userdict = shop_details.objects.all()
    return render(request, 'shop_detailsview.html', {'userdict': userdict})


# Complaints functions
def insertcomplaints(request):
    if request.method == "POST":
        complant_id = request.POST.get('t1')
        give_by = request.POST.get('t2')
        details = request.POST.get('t3')
        date = request.POST.get('t4')
        status = request.POST.get('t5')
        complaints.objects.create(
            complant_id=complant_id, give_by=give_by, details=details,
            date=date, status=status
        )
        return render(request, 'insertcomplaints.html')
    return render(request, 'insertcomplaints.html')

def complaintsview(request):
    userdict = complaints.objects.all()
    return render(request, 'complaintsview.html', {'userdict': userdict})


# Service Details functions
def insertservicedetails(request):
    if request.method == "POST":
        service_id = request.POST.get('t1')
        service_type = request.POST.get('t2')
        details = request.POST.get('t3')
        cost = request.POST.get('t4')
        contact_no = request.POST.get('t5')
        servicedetails.objects.create(
            service_id=service_id, service_type=service_type, details=details,
            cost=cost, contact_no=contact_no
        )
        return render(request, 'insertservicedetails.html')
    return render(request, 'insertservicedetails.html')

def servicedetailsview(request):
    userdict = servicedetails.objects.all()
    return render(request, 'servicedetailsview.html', {'userdict': userdict})


# Incharge Details functions
def insertincharge_details(request):
    if request.method == "POST":
        work_type = request.POST.get('t1')
        incharge_name = request.POST.get('t2')
        contact_no = request.POST.get('t3')
        form_date = request.POST.get('t4')
        till_date = request.POST.get('t5')
        timing = request.POST.get('t6')
        incharge_details.objects.create(
            work_type=work_type, incharge_name=incharge_name, contact_no=contact_no,
            form_date=form_date, till_date=till_date, timing=timing
        )
        return render(request, 'insertincharge_details.html')
    return render(request, 'insertincharge_details.html')

def incharge_detailsview(request):
    userdict = incharge_details.objects.all()
    return render(request, 'incharge_detailsview.html', {'userdict': userdict})


# Food Store functions
def insertFood_store(request):
    if request.method == "POST":
        store_name = request.POST.get('t1')
        food_type = request.POST.get('t2')
        timing = request.POST.get('t3')
        contact_no = request.POST.get('t4')
        rating = request.POST.get('t5')
        Food_store.objects.create(
            store_name=store_name, food_type=food_type, timing=timing,
            contact_no=contact_no, rating=rating
        )
        return render(request, 'insertFood_store.html')
    return render(request, 'insertFood_store.html')

def Food_storeview(request):
    userdict = Food_store.objects.all()
    return render(request, 'Food_storeview.html', {'userdict': userdict})


# Register functions
def insertRegister(request):
    if request.method == "POST":
        username = request.POST.get('t1')
        email_id = request.POST.get('t2')
        city_type = request.POST.get('t3')
        country = request.POST.get('t4')
        moblie_no = request.POST.get('t5')
        date = request.POST.get('t6')

        user = Register.objects.filter(email_id=email_id).count()
        if user >= 1:
            return render(request, 'registration.html', {'msg': 'user is already exist'})
        else:
            Register.objects.create(
                username=username, email_id=email_id, city_type=city_type,
                country=country, moblie_no=moblie_no, date=date
            )
            UserLogin.objects.create(username=username, password="123123", utype='user')
        return render(request, 'insertRegister.html')
    return render(request, 'insertRegister.html')

def Registerview(request):
    userdict = Register.objects.all()
    return render(request, 'Registerview.html', {'userdict': userdict})
