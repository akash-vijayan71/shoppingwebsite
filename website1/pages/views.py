from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader 
from . models import Contact,Register,Product,Cart,Order,Adminlogin,Category,Wishlist
from django.contrib import messages

# Create your views here.

def index(request):
    category=Category.objects.all().values()

    context={
        'category':category
    }
    
    template=loader.get_template("index.html")
    return HttpResponse(template.render(context,request))
def about(request):
    template=loader.get_template("about.html")
    return HttpResponse(template.render({},request))
def contact(request):
    if request.method == 'POST':
        contact_name = request.POST["contact_name"]
        contact_email = request.POST["contact_email"]
        contact_message= request.POST["contact_message"]

        contact = Contact(contact_name=contact_name,
                          contact_email=contact_email,
                          contact_message=contact_message)
        contact.save()

    template=loader.get_template("contact.html")
    return HttpResponse(template.render({},request))
def service(request):
    template=loader.get_template("service.html")
    return HttpResponse(template.render())
def register(request):
    if "user" in request.session:
        return HttpResponseRedirect("/acount")
    if request.method == 'POST':
        reg_name = request.POST["reg_name"]
        reg_email = request.POST["reg_email"]
        reg_num = request.POST["reg_num"]
        reg_uname = request.POST["reg_uname"]
        reg_pswrd = request.POST["reg_pswrd"]

        same=Register.objects.filter(reg_email=reg_email,
                                     reg_name=reg_name,
                                     reg_uname=reg_uname)
        if same:
            messages.success(request,"User already exists!")
            return HttpResponseRedirect("/register")
        else:
            register = Register(reg_name=reg_name,
                            reg_email=reg_email,
                            reg_num=reg_num,
                            reg_uname=reg_uname,
                            reg_pswrd=reg_pswrd)
        
        register.save()
    

    template=loader.get_template("register.html")
    return HttpResponse(template.render({},request))

def login(request):
    if "user" in request.session:
        return HttpResponseRedirect('/acount')
    if request.method == 'POST':
         log_uid=request.POST["log_uid"]
         log_pwd=request.POST["log_pwd"]

         login = Register.objects.filter(reg_uname=log_uid,reg_pswrd=log_pwd)
         if login:
            request.session["user"]=log_uid
            return HttpResponseRedirect('/index')

    template=loader.get_template("login.html")
    return HttpResponse(template.render({},request))

def profile(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")

    template=loader.get_template("profile.html")
    return HttpResponse(template.render({},request))
def logout(request):
    if 'user' in request.session:
        del request.session["user"]
    return HttpResponseRedirect("/login")
def addproduct(request):
    if 'adminuser' not in request.session:
        return HttpResponseRedirect("/adminlogin")
    if request.method=="POST":
        p_name=request.POST["p_name"]
        p_price=request.POST["p_price"]
        p_image=request.FILES["p_image"]
        p_category=request.POST["p_category"]

        product=Product(p_name=p_name,
                        p_price=p_price,
                        p_image=p_image,
                        p_category=p_category)
        product.save()
    category=Category.objects.all().values()

    context={
        'category':category
    }
    template=loader.get_template("addproduct.html")
    return HttpResponse(template.render(context,request))
def products(request):
    products=Product.objects.all().values()

    context={
        'products':products
    }

    template=loader.get_template("products.html")
    return HttpResponse(template.render(context,request))
def cart(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")
    chk = Order.objects.filter(odr_user=request.session["user"],odr_status=0)
    for x in chk:
        x.delete()
    

    if request.method=='POST':
        q=request.POST["qty"]
        cid=request.POST["cid"]
        ccart=Cart.objects.filter(id=cid)[0]
        if q=='+':
            ccart.cp_qty+=1
            ccart.cp_amount=ccart.cp_disprice*ccart.cp_qty
        elif q=='-':
            ccart.cp_qty-=1
            ccart.cp_amount=ccart.cp_disprice*ccart.cp_qty
      
        ccart.save()

    cart=Cart.objects.all().values()

    cart2=Cart.objects.all()

    total=0
    for x in cart2:
         total+=x.cp_disprice

    context={
        'cart':cart,
        'total':total
        }
    

    template=loader.get_template("cart.html")
    return HttpResponse(template.render(context,request))
def addtocart(request,id):
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")
    dcart=Cart.objects.filter(cp_pid=id)
    if dcart:
        for x in dcart:
            x.cp_qty+=1
            x.cp_amount=x.cp_price*x.cp_qty
            x.save()
    else:
        pro=Product.objects.filter(id=id)[0]
        cart = Cart(
                    cp_user=request.session["user"],
                    cp_name=pro.p_name,
                    cp_price=pro.p_price,
                    cp_image=pro.p_image,
                    cp_qty=1,
                    cp_amount=pro.p_disprice,
                    cp_pid=id,
                    cp_disprice=pro.p_disprice)
        cart.save()
    return HttpResponseRedirect("/cart") 
def addtocheckout(request):
    cart=Cart.objects.all()
    for x in cart:

        order = Order(
                    odr_user=x.cp_user,
                    odr_name=x.cp_name,
                    odr_price=x.cp_price,
                    odr_image=x.cp_image,
                    odr_qty=x.cp_qty,
                    odr_amount=x.cp_amount,
                    odr_disprice=x.cp_disprice,
                    odr_status=0)
    
        order.save()
    return HttpResponseRedirect("/checkout")
def checkout(request):
    order=Order.objects.filter(odr_user=request.session["user"],odr_status=0).values()
    order2=Order.objects.filter(odr_user=request.session["user"],odr_status=0)

    total=0
    for x in order2:
         total+=x.odr_amount
    context={
          'order':order,
          'total':total
    } 

    template=loader.get_template("checkout.html")
    return HttpResponse(template.render(context,request))  
def confirmorder(request):
    if request.method=='POST':
        on=request.POST["on"]
        oa=request.POST["oa"]
        op=request.POST["op"]
        oe=request.POST["oe"]
        py=request.POST["payment"]
    
        order=Order.objects.filter(odr_user=request.session["user"],odr_status=0)

        for x in order:
            x.odr_billname=on
            x.odr_address=oa
            x.odr_email=oe
            x.odr_phone=op
            x.odr_status=1
            x.odr_type=py
            x.save()
    template=loader.get_template("confirmorder.html")
    return HttpResponse(template.render({},request))  
def deletecart(request,id):

    d=Cart.objects.filter(id=id)[0]

    d.delete()

    return HttpResponseRedirect("/cart")
def adminlogin(request):
    if request.method=='POST':
        ad_uname=request.POST['ad_uname']
        ad_pwd=request.POST['ad_pwd']

        adminlogin = Adminlogin.objects.filter(
                                ad_uname=ad_uname,
                                ad_pwd=ad_pwd)
        
        if adminlogin:
            request.session["adminuser"]=ad_uname
            return HttpResponseRedirect("/adminpage")
    template=loader.get_template("adminlogin.html")
    return HttpResponse(template.render({},request))
def adminlogout(request):
    del request.session["adminuser"]
    return HttpResponseRedirect("/adminlogin")
def adminpage(request):
    products=Product.objects.all().values()

    context={
        'products':products
    }
    template=loader.get_template("adminpage.html")
    return HttpResponse(template.render(context,request))
def adminproducts(request):
    template=loader.get_template("adminproducts.html")
    return HttpResponse(template.render({},request))
def deleteproduct(request,id):

    ad=Product.objects.filter(id=id)[0]

    ad.delete()

    return HttpResponseRedirect("/adminpage")
def editproduct(request,id):
    if request.method == 'POST':
        pro_name=request.POST["pro_name"]
        pro_price=request.POST["pro_price"]
        pro_description=request.POST["pro_description"]
        pro_disprice=request.POST["pro_disprice"]
        prod=Product.objects.filter(id=id)[0]
        prod.p_name=pro_name
        prod.p_price=pro_price
        prod.p_description=pro_description
        prod.p_disprice=pro_disprice       

        if len(request.FILES) != 0:
            pro_image=request.FILES["pro_image"]
            prod.p_image=pro_image
        prod.save()

    product=Product.objects.filter(id=id).values()
    context={
        'product':product
    }
    template=loader.get_template("editproduct.html")
    return HttpResponse(template.render(context,request))
def editcategory(request):
    template=loader.get_template("editcategory.html")
    return HttpResponse(template.render())
def addcategory(request):
    if request.method=='POST':
        c_name=request.POST["c_name"]
        c_image=request.FILES["c_image"]

        category=Category(c_name=c_name,
                          c_image=c_image)

        category.save()
    template=loader.get_template("addcategory.html")
    return HttpResponse(template.render({},request))
def category(request):
    category=Category.objects.all().values()

    context={
        'category':category
    }
    
    template=loader.get_template("category.html")
    return HttpResponse(template.render(context,request))

def cat(request,id):

    products=Product.objects.filter(p_category=id).values()
    context={
        'products':products
    }
    template=loader.get_template("products.html")
    return HttpResponse(template.render(context,request))
def wishlist(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")
    wishlist=Wishlist.objects.all().values()

    context={
        'wishlist':wishlist
    }

    template=loader.get_template("wishlist.html")
    return HttpResponse(template.render(context,request))
def addtowishlist(request,id):
    pro=Product.objects.filter(id=id)[0]

    wishlist=Wishlist(w_image=pro.p_image,
                      w_name=pro.p_name,
                      w_price=pro.p_price,
                      w_stock=str("In Stock"))
    wishlist.save()
    return HttpResponseRedirect("/wishlist")