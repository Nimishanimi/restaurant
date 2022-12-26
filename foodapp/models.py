from django.db import models








################################# ADMIN #################################################
class admreg_tb(models.Model):
	admname = models.CharField(max_length=255)
	admemail = models.CharField(max_length=255)
	admpassword = models.CharField(max_length=255)

class menu_tb(models.Model):
	Fname=models.CharField(max_length=255)
	fdescription=models.TextField()
	fimg=models.ImageField(upload_to="product/")


class reservation_tb(models.Model):
	uid= models.ForeignKey(menu_tb, on_delete=models.CASCADE)
	rname=models.CharField(max_length=255)
	remail=models.CharField(max_length=255)
	rphone=models.CharField(max_length=255)
	raddress=models.CharField(max_length=255)
	rcity=models.CharField(max_length=255)
	rstate=models.CharField(max_length=255)
	rzipcode=models.CharField(max_length=255)

class galleryup_tb(models.Model):
	gname=models.CharField(max_length=255)
	gimg=models.ImageField(upload_to="product/")

	