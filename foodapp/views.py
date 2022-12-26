from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from foodapp.models import *
import os   
import random
import string
from django.conf import settings
from django.core.mail import send_mail

def index(request):
	return render(request,'index.html')
def about(request):
	return render(request,'about.html')
def menu(request):
	data= menu_tb.objects.all()
	return render(request,'menu.html',{"user":data})
def viewdetails(request):
	# if request.session.has_key("myid"):
		pid=request.GET['uid']
		check=menu_tb.objects.filter(id=pid)
		return render(request,'viewdetails.html',{"user":check})
	# else:
	# 	return render(request,'menu.html')
def gallery(request):
	gal=galleryup_tb.objects.all()
	return render(request,'gallery.html',{"user":gal})
def contact(request):
	return render(request,'contact.html')
		
	

def userdetails(request):
	if request.method=='POST':
		pid=request.GET['uid']
		uname=request.POST['resname']
		uemail=request.POST['w3lSender']
		uphone=request.POST['w3lPhone']
		uaddress=request.POST['add']
		ucity=request.POST['cit']
		ustate=request.POST['stat']
		uzipcode=request.POST['zip']
		click=menu_tb.objects.get(id=pid)
		d=menu_tb.objects.filter(id=pid)
		for x in d:
			name=x.Fname
		
		new=reservation_tb(rname=uname,remail=uemail,rphone=uphone,raddress=uaddress ,rcity=ucity,rstate=ustate,rzipcode=uzipcode,uid=click)
		new.save()
		x = ''.join(random.choices(uname + string.digits, k=8))
		y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
		subject = 'enquiry from customer'
		message = f'Hi , There is an enquiry from the customer'
		email_from = settings.EMAIL_HOST_USER 
		recipient_list = [uemail, ] 
		send_mail( subject, message, email_from, recipient_list )
		subject = 'welcome to BBQ@PARAMOUNT'
		message = f'Hi {uname}, your emailid: {uemail}. your {name} hasbeen reserved Successfully.Have a yummy day!'
		email_from = settings.EMAIL_HOST_USER 
		recipient_list = [uemail, ] 
		send_mail( subject, message, email_from, recipient_list )
		return render(request,'index.html')
	else:
		pid=request.GET['uid']
		return render(request,'userdetails.html',{"pid":pid})


	







######################################## ADMIN ######################################################################################


def admin_index(request):
	return render(request,"admin/index.html")
def forms(request):
	if request.method=='POST':
		rname=request.POST['proname']
		rdescription=request.POST['prodesc']
		rimages=request.FILES['proimages']
		check=menu_tb.objects.filter(Fname=rname)
		if check:
			return render(request,'admin/forms.html',)
		else:
			add=menu_tb(Fname=rname,fdescription=rdescription,fimg=rimages)
			add.save()
			return render(request,"admin/forms.html")
	else:
		return render(request,"admin/forms.html")
def formedit(request):
	newedit=menu_tb.objects.all()
	return render(request,'admin/formtable.html',{"user":newedit})
def formdelete(request):
	pid=request.GET['uid']
	data=menu_tb.objects.filter(id=pid).delete()
	return HttpResponseRedirect('/forms/')
def formupdate(request):
	if request.method =="POST":
		rname=request.POST['proname']
		rdescription=request.POST['prodesc']
		pid=request.GET['tid']
		img=request.POST['img']
		if img =="yes":
			rimages=request.FILES['proimages']
			old=menu_tb.objects.filter(id=pid)
			new=menu_tb.objects.get(id=pid)
			for x in old:
				fimg=x.fimg.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+fimg
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			new.fimg=rimages
			new.save()
		add=menu_tb.objects.filter(id=pid).update(Fname=rname,fdescription=rdescription,fimg=rimages)
			
		return HttpResponseRedirect('/formedit/')
	else:
		pid=request.GET['tid']
		newedit=menu_tb.objects.filter(id=pid)
		return render(request,'admin/produpdate.html',{"user":newedit})


def admlogin(request):
	if request.method == "POST":
	 	aemail=request.POST['remail']
	 	apassword=request.POST['rPassword']
	 	check=admreg_tb.objects.filter(admemail=aemail,admpassword=apassword)
	 	if check:
	 		for x in check:
	 			request.session['myid']=x.id
	 			request.session['myname']=x.admname 
	 		return render(request,'admin/index.html',)
	 	else:
	 		return render(request,'admin/login.html',)
	else:
		return render(request,"admin/admlogin.html")
def admsignup(request):
	# data=admreg_tb.objects.all()
	if request.method == "POST":
		aname=request.POST["rname"]
		aemail=request.POST["remail"]
		apassword=request.POST["rPassword"]
		check= admreg_tb.objects.filter(admemail=aemail)
		if check:
			return HttpResponseRedirect('/adminindex/')
		else:
			add=admreg_tb(admname=aname,admemail=aemail,admpassword=apassword)
			add.save()
			return render(request,"admin/admsignup.html")

	else:
		return render(request,"admin/admsignup.html")
def admin_logout(request):
	if request.session.has_key('myid'):
		del request.session['myname']
		del request.session['myid']
		return HttpResponseRedirect('/')


def galleryupload(request):
	if request.method=='POST':
		name=request.POST['galname']
		images=request.FILES['galimages']
		check=galleryup_tb.objects.filter(gname=name)
		if check:
			return render(request,'admin/galleryupload.html',)
		else:
			add=galleryup_tb(gname=name,gimg=images)
			add.save()
			return render(request,"admin/galleryupload.html")
	else:
		return render(request,"admin/galleryupload.html")
