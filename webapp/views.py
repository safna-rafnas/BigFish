from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import products_db,recipie_db,category_db
from webapp.models import regdb,Cart,orders,Contact_db
from django.views.decorators.csrf import csrf_exempt
from django.db.models.aggregates import Sum
from django.core.mail import send_mail
from BIGFISH import settings
# Create your views here.

def home(request):
    c=Cart.objects.filter(userid=request.session.get('userid'),status=0).count()
    data1=category_db.objects.all()
    data=products_db.objects.all()
    return render(request,'home.html',{'data1':data1,'data':data,'c':c})

def about(request):
    c=Cart.objects.filter(userid=request.session.get('userid')).count()
    return render(request,'about.html')

def products(request,cat):
    print(cat)
    if (cat=="all"):
        d=products_db.objects.all()
    else:
        d=products_db.objects.filter(categ=cat)
    return render(request,'products.html',{'d':d})
    

def recipes(request):
    data=recipie_db.objects.all()
    print(data)
    return render(request,'recipes.html',{'data':data})

def showrecipe(request,dataid):
    data=recipie_db.objects.filter(id=dataid)
    print(data)
    return render(request,'showrecipe.html',{'data':data})  

def myaccount(request):
    return render(request,'myaccount.html')

def register(request):
    return render(request,'register.html')


def regdata(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        mobileno=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        obj=regdb(name=name,mobileno=mobileno,email=email,password=password)
        obj.save()
        return redirect("myaccount")
    
def logindata(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('pass')
        if regdb.objects.filter(email=email,password=password).exists():
            data=regdb.objects.filter(email=email,password=password).values('name','email','mobileno','id').first()
            request.session['uname']=data['name']
            request.session['pass']=password
            request.session['email']=data['email']
            request.session['phonenumber']=data['mobileno']
            request.session['userid']=data['id']
            return redirect('home')
            # return redirect('cart1',args=(prodid,))
        else:
            return HttpResponse("username is invalid")

def logout(request):
        del request.session['uname']
        del request.session['pass']
        del request.session['email']
        del request.session['phonenumber']
        del request.session['userid']
        return redirect('home')

def productdetail(request,dataid):
    data=products_db.objects.filter(id=dataid)
    return render(request,'productdetail.html',{'data':data})

def cart1(request,prodid):
    if 'userid' in request.session.keys():
        if Cart.objects.filter(productid=prodid,status=0,userid=request.session.get('userid')).exists():
            quantity=request.POST.get('quan')
            total=request.POST.get('tot_amount')
            userid=request.POST.get('userid')
            Cart.objects.filter(productid=prodid,status=0).update(Total=total,quantity=quantity)
            return redirect('mycart')
        else:
            quantity=request.POST.get('quan')
            total=request.POST.get('tot_amount')
            userid=request.POST.get('userid')
            print("*******************************************")
            print(userid)
            obj=Cart(productid=products_db.objects.get(id=prodid),Total=total,quantity=quantity,userid=regdb.objects.get(id=userid),status=0)
            obj.save()
            return redirect('mycart')
    else:
        return redirect('myaccount')

@csrf_exempt    
def cartupdate(request):
    if request.method == 'POST':
        cartid=request.POST.get('pid')
        q=request.POST.get('qty')
        p=request.POST.get('price')
        T=int(q)*int(p)
        Cart.objects.filter(id=cartid).update(quantity=q,Total=T)
        return HttpResponse()  
    
def mycart(request):
    if 'userid' in request.session.keys():
        co=request.session.get('userid')
        cartob=Cart.objects.filter(userid=co,status=0)
        c=Cart.objects.filter(userid=co,status=0).count()
        subtotal=Cart.objects.filter(userid=co,status=0).aggregate(Sum('Total'))
        s=subtotal['Total__sum']
        return render(request,'mycart.html',{'cartob':cartob ,'s':s,'c':c})
    else:
        return redirect('myaccount')

def deletecart(request,dataid):
    Cart.objects.filter(id=dataid).delete()
    return redirect('mycart')

def checkout(request):
    co=request.session.get('userid')
    c=Cart.objects.filter(userid=co,status=0).count()
    cartob=Cart.objects.filter(userid=co,status=0)
    subtotal=Cart.objects.filter(userid=co,status=0).aggregate(Sum('Total'))
    s=subtotal['Total__sum']
    return render(request,'checkout.html',{'s':s,'c':c,'cartob':cartob})

def orders_db(request):
    name_r = request.POST.get('firstName')
    user_r = request.POST.get('username')
    email_r = request.POST.get('email')
    address_r = request.POST.get('address')
    country_r = request.POST.get('country')
    state_r = request.POST.get('state')
    zip_r = request.POST.get('zip')
    c=request.session.get('userid')
    print(c)
    cartob=Cart.objects.filter(userid=c,status=0)
    print(cartob)
    for a in cartob:
        obj=orders(cartid=Cart.objects.get(id=a.id),Firstname=name_r,username=user_r,email=email_r,address=address_r,country=country_r,state=state_r,zipcode=zip_r)      
        obj.save()
        Cart.objects.filter(id=a.id).update(status=1)     
    return redirect('home')


def reset_password(request):
    return render(request,'password_reset_form.html')

def password(request):
    if request.method == "POST":
        email=request.POST.get('email')
        subject="Forgot password"
        link="http://127.0.0.1:8000/passwordform"
        from_email=settings.DEFAULT_FROM_EMAIL
        send_mail(subject,link,from_email,[email],fail_silently=False)
        return HttpResponse("done")

def passwordform(request):
    return render(request,'resetform.html')

def pricerange(request):
    if request.method == 'POST':
        filter_price1 = request.GET.get('price-min')
        filter_price2 = request.GET.get('price_max')
        print(filter_price1)
        print(filter_price2)

def contact(request):
    return render(request,'contact.html')

def contactdata(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact_db(name=name, email=email, subject=subject, message=message)
        data.save()
        return redirect('home')