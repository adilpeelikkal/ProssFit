from django.shortcuts import render

# Create your views here.

def AboutUs(request):
	return render(request,'guest/activar/about-us.html')

def Schedule(request):
	return render(request,'guest/activar/schedule.html')

def Gallery(request):
	return render(request,'guest/activar/gallery.html')

def Contact(request):
	return render(request,'guest/activar/contact.html')
