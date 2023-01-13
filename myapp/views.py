from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import products_db,recipie_db,category_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.models import *

# Create your views here.
def my(request):
    usercount = regdb.objects.all().count()
    productcount = products_db.objects.all().count()
    categorycount = category_db.objects.all().count()
    odercount =  orders.objects.all().count()
    return render(request,'base.html', {'usercount': usercount, 'productcount': productcount, 'categorycount':categorycount, 'odercount':odercount})
   
def addproduct(request):
    # data=products_db.objects.all()
    da=category_db.objects.all()
    return render(request,'addproduct.html',{'da':da})

def productdatas(request):
    if request.method == 'POST':
        name_r=request.POST.get('name')
        weight_r=request.POST.get('weight')
        categ=request.POST.get('categ')
        price_r= request.POST.get('price')
        image_r=request.FILES['file1']
        obj=products_db(name=name_r,weight=weight_r,categ=categ,price=price_r,image=image_r)
        obj.save()
        # print(obj)
        return redirect('viewproducts')

def viewproducts(request):
    datas=products_db.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(datas, 6)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request,'viewproducts.html',{"data":data})

def deleteproducts(request):
    if request.method == 'POST':
        dataid            = request.POST.get('data_id')
        products_db.objects.filter(id=dataid).delete()
        return redirect('viewproducts')

def editproducts(request,dataid):
    data=products_db.objects.filter(id=dataid)
    return render(request,'editproduct.html',{'data':data}) 

def updateproducts(request,dataid):
    if request.method == 'POST':
        name_r=request.POST.get('name')
        weight_r=request.POST.get('weight')
        price_r= request.POST.get('price')
        try:
            image_r=request.FILES['file1']
            fs = FileSystemStorage() 
            file = fs.save(image_r.name, image_r)
        except MultiValueDictKeyError :
            file=products_db.objects.get(id=dataid).image
        products_db.objects.filter(id=dataid).update(name=name_r,weight=weight_r,price=price_r,image=file)
        return redirect('viewproducts')

def addrecipies(request):
    return render(request,'addrecipies.html')

def recipiedatas(request):
    if request.method == 'POST':
        recipiename_r=request.POST.get('recipiename')
        ingredients_r=request.POST.get('ingredients')
        instructions_r= request.POST.get('instructions')
        image_r=request.FILES['file1']
        obj=recipie_db(recipiename=recipiename_r,ingredients=ingredients_r,instructions=instructions_r,image=image_r)
        obj.save()
        print(obj)
        return redirect('addrecipies')

def viewrecipies(request):
    data=recipie_db.objects.all()
    return render(request,'viewrecipies.html',{"data":data})

def deleterecipies(request):
    if request.method == 'POST':
        dataid            = request.POST.get('data_id')
        recipie_db.objects.filter(id=dataid).delete()
        return redirect('viewrecipies')

def editrecipies(request,dataid):
    data=recipie_db.objects.filter(id=dataid)
    return render(request,'editrecipie.html',{'data':data})

def updaterecipies(request,dataid):
    recipiename_r=request.POST.get('recipiename')
    ingredients_r=request.POST.get('ingredients')
    instructions_r= request.POST.get('instructions')
    try:
        image_r=request.FILES['file1']
        fs = FileSystemStorage() 
        file = fs.save(image_r.name, image_r)
    except MultiValueDictKeyError :
        file=recipie_db.objects.get(id=dataid).image
    recipie_db.objects.filter(id=dataid).update(recipiename=recipiename_r,ingredients=ingredients_r,instructions=instructions_r,image=file)
    return redirect('viewrecipies')

def customers(request):
    data = regdb.objects.all()
    return render(request,'customers.html',{'data':data})

def order(request):
    data = orders.objects.all()
    return render(request,'orders.html',{'data':data})

def cart(request):
    data = Cart.objects.filter(status=0)
    return render(request, 'cart.html',{'data':data})

def categorydescription(request):
    return render(request,'addcategories.html')

def categorydatas(request):
    data=dict()
    if request.method == 'POST':
        catname=request.POST.get('cname')
        catdesc=request.POST.get('cdescription')
        image_r=request.FILES['file']
        obj=category_db(cname=catname,catdescpn=catdesc,image=image_r)
        obj.save()
        data['message']="Succesfully Registered"
        data['error']=1
        return JsonResponse(data)

def viewcategory(request):
    data=category_db.objects.all()
    return render(request,'viewcategories.html',{"data":data})

def deletecategory(request,dataid):
        category_db.objects.filter(id=dataid).delete()
        return redirect('viewcategory')

def editcategory(request,dataid):
    data=category_db.objects.filter(id=dataid)
    return render(request,'editcategory.html',{'data':data})

def updatecategory(request,dataid):
    cname_r=request.POST.get('cname')
    desc_r=request.POST.get('cdescription')
    try:
        image_r=request.FILES['file']
        fs = FileSystemStorage() 
        file = fs.save(image_r.name, image_r)
    except MultiValueDictKeyError :
        file=category_db.objects.get(id=dataid).image
    category_db.objects.filter(id=dataid).update(cname=cname_r,catdescpn=desc_r,image=file)
    return redirect('viewcategory')

def message(request):
    data = Contact_db.objects.all()
    return render(request,'message.html',{'data':data})

def adminlogin(request):
    return render(request,'adminlogin.html')

def adlogin(request):
    username_r = request.POST.get('username')
    password_r = request.POST.get('password')
    print(username_r)
    print(password_r)
    if User.objects.filter(username__contains=username_r).exists():
        user = authenticate(username=username_r,password=password_r)
        if user is not None:
            login(request,user)
            request.session['username'] = username_r
            request.session['password'] = password_r
            print(user)
            return redirect('my')
        else:
            return render(request,'adminlogin.html',{'msg':'Sorry....Invalid user credentials'})
    else:
        return render(request,'adminlogin.html',{'msg':'Sorry....Invalid user credentials'})

def adlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('adminlogin')