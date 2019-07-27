from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args,**kwargs):
	print(request.user)
	print(args)
	print(kwargs)
	return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
	my_dict={
	"my_text":"Shivam Chand Deopa",
	"my_num":7,
	"my_list":[1,2,3,4,5,6,7]
	}
	return render(request,"contact.html",my_dict)