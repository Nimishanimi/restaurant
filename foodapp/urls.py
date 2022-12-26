from django.urls import path
from foodapp import views

urlpatterns=[
 path("",views.index),
 path('about/',views.about),
 path('menu/',views.menu),
 path('viewdetails/',views.viewdetails),

 path('gallery/',views.gallery),
 path('contact/',views.contact),
 path('userdetails/',views.userdetails),
 
 



################################## ADMIN ##############################################
path('adminindex/',views.admin_index),
path('forms/',views.forms),
path('formedit/',views.formedit),
path('formdelete/',views.formdelete),
path('formupdate/',views.formupdate),

path('admlogin/',views.admlogin),
path('admsignup/',views.admsignup),
path('galleryupload/',views.galleryupload),







]