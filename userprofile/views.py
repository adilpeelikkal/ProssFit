from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View
from userprofile.models import UserProfile
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
import sys 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.template import loader, Context
import secrets
# Create your views here.

class GuestSection(View):
	def get(self, request):
		return render(request,'guest/activar/index.html')

class Registration(View):
	def get(self, request):
		return render(request,'Login_v10/index.html')
class UserLogin(View):
	def post(self, request):
		if request.method=='POST':
			uname=request.POST['username']
			password=request.POST['password']
			user = authenticate(username=uname, password=password)
			print(user)
			if user is not None:
				return render(request,'Login_v10/welcome.html',{'user':user})
			else:
				return HttpResponse('Invalid credentials')

class UserSignup(View):
	def get(self, request):
		return render(request, 'Login_v10/signup.html')

class UserRegister(View):
	def post(self,request):
		if request.method=='POST':
			name=request.POST['name']
			password=request.POST['password']
			email=request.POST['email']
			token=None
			if User.objects.filter(email=email).exists():
				print("yftydr")
				# return HttpResponse("This email already exist")
				return HttpResponse(json.dumps({'success': False, 'register': '','msg':'This email already exist'}, cls=DjangoJSONEncoder), status=200)

			else:
				register = User.objects.create_user(username=name, password=password, email=email)
				data = serializers.serialize('json', [register])
				return HttpResponse(json.dumps({'success': True, 'register': data,'msg':''}, cls=DjangoJSONEncoder), status=200)

		

class ForgotPassword(View):
	def get(self, request):
		return render(request,'Login_v10/forgotpwd.html')

	def post(self,request):
		if request.method=='POST':
			email=request.POST['email']
			APP_NAME = "actionfi"
			base_url = 'http://127.0.0.1:8000/'
			token = secrets.token_urlsafe()
			user = User.objects.get(email=email)
			try:
				user = User.objects.get(email=email)
			except:
				return HttpResponse('No such user')

			try:
				userprofile = UserProfile.objects.get(user=user)
			except:
				userprofile = UserProfile.objects.create(user=user)
			if userprofile:
				userprofile.token = token
				userprofile.save()

			html_message = loader.render_to_string( 'Login_v10/reset_password.html', {'email': email, 'login_url':base_url, 'token':token} )
			send_mail('Reset Password', '', APP_NAME + ' <do_not_reply@domain.com>', [ email], fail_silently=True, html_message=html_message)

		return HttpResponse('done')

class ConfirmPassword(View):
	def get(self, request):
		token = request.GET.get('token')
		print(token)
		return render(request,'Login_v10/confirm_pwd.html',{'token':token})

	def post(self, request):
		if request.method=='POST':
			token=None
			newpwd = request.POST['newpwd']
			conpwd = request.POST['cpwd']
			if newpwd==conpwd:
				token = self.request.GET.get('token')
				try:
					userprofile = UserProfile.objects.get(token=token)
				except:
					return HttpResponse("you dont have access to reset password")
				else:
					user = User.objects.get(id=userprofile.user.id)
					user.set_password(newpwd)
					print(user.password)
					user.save()
					UserProfile.objects.filter(user=user).delete()
			else:
				return HttpResponse("please confirm password")
		return render(request,'Login_v10/index.html')
