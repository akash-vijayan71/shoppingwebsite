from django.db import models



# Create your models here.

class Contact(models.Model):
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)
    contact_message = models.TextField(null=True)
   
    def __str__(self):
        return self.contact_name
class Register(models.Model):
    reg_name = models.CharField(max_length=255)
    reg_email = models.EmailField(max_length=255)
    reg_num = models.CharField(max_length=255)
    reg_uname = models.CharField(max_length=255)
    reg_pswrd = models.CharField(max_length=255)

    def __str__(self):
        return self.reg_name
    
class Product(models.Model):
    p_name = models.CharField(max_length=255)
    p_price = models.FloatField()
    p_image = models.FileField(upload_to='products')
    p_category = models.CharField(max_length=255,null=True)
    p_description = models.CharField(max_length=255,null=True)
    p_disprice = models.FloatField(null=True)

    def __str__(self):
        return self.p_name

class Cart(models.Model):
    cp_user = models.CharField(max_length=255,null=True)
    cp_name = models.CharField(max_length=255)
    cp_price = models.FloatField()
    cp_image = models.FileField()
    cp_qty = models.IntegerField()
    cp_amount = models.FloatField()
    cp_pid = models.CharField(max_length=255,null=True)
    cp_disprice = models.FloatField(null=True)

    def __str__(self):
        return self.cp_name
class Order(models.Model):
    odr_user = models.CharField(max_length=255,null=True)
    odr_name = models.CharField(max_length=255)
    odr_price = models.FloatField()
    odr_image = models.FileField()
    odr_qty = models.IntegerField()
    odr_amount = models.FloatField()
    odr_status = models.IntegerField(null=True)
    odr_billname=models.CharField(max_length=255,null=True)
    odr_address=models.CharField(max_length=255,null=True)
    odr_email=models.EmailField(null=True)
    odr_phone=models.IntegerField(null=True)
    odr_type=models.CharField(max_length=10,null=True)
    odr_disprice=models.FloatField(null=True)

    def __str__(self):
        return self.odr_name
    
class Adminlogin(models.Model):
    ad_name=models.CharField(max_length=255,null=True)
    ad_uname=models.CharField(max_length=255)
    ad_pwd=models.CharField(max_length=255)

    def __str__(self) :
        return self.ad_uname

class Category(models.Model):
    c_name=models.CharField(max_length=255,null=True)
    c_image=models.FileField()

    def __str__(self) :
        return self.c_name
class Wishlist(models.Model):
    w_name=models.CharField(max_length=255)
    w_price=models.FloatField()
    w_stock=models.CharField(max_length=255)
    w_image=models.FileField(null=True)

    def __str__(self) :
        return self.w_name