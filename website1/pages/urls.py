from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.index,name="index"),
    path("index",views.index,name="index"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("service",views.service,name="service"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("profile",views.profile,name="profile"),
    path("logout",views.logout,name="logout"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("products",views.products,name="products"),
    path("cart",views.cart,name="cart"),
    path("addtocart/<int:id>",views.addtocart,name="addtocart"),
    path("checkout",views.checkout,name="checkout"),
    path("addtocheckout",views.addtocheckout,name="addtocheckout"),
    path("checkout",views.checkout,name="checkout"),
    path("confirmorder",views.confirmorder,name="confirmorder"),
    path("deletecart/<int:id>",views.deletecart,name="deletecart"),
    path("adminlogin",views.adminlogin,name="adminlogin"),
    path("adminlogout",views.adminlogout,name="adminlogout"),
    path("adminpage",views.adminpage,name="adminpage"),
    path("adminproducts",views.adminproducts,name="adminproducts"),
    path("deleteproduct/<int:id>",views.deleteproduct,name="deleteproduct"),
    path("editproduct/<int:id>",views.editproduct,name="editproduct"),
    path("editcategory",views.editcategory,name="editcategory"),
    path("addcategory",views.addcategory,name="addcategory"),
    path("category",views.category,name="category"),
    path("cat/<int:id>",views.cat,name="cat"),
    path("addtowishlist/<int:id>",views.addtowishlist,name="addtowishlist"),
    path("wishlist",views.wishlist,name="wishlist"),
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)