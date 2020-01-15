from django.shortcuts import render
import players.views
from players.models import Player 
from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from django.core.files.storage import FileSystemStorage

# Create your views here.
class PlayersDetails(View):
	def get(self, request):
		players = Player.objects.all()
		return render(request,'Table_Responsive_v2/index.html',{'players':players})

class PlayersRegistration(View):
	def get(self, request):
		return render(request,'Table_Responsive_v2/player_contact_form.html')
	def post(self, request):
		if request.method == 'POST':
			email = request.POST['email']
			if Player.objects.filter(email=email).exists():
				print("2")
				return HttpResponse("This email alraedy exist")
			else:
				print("asdf")
				player, created = Player.objects.get_or_create(email=email)
				if created:
					player.first_name = request.POST['first_name']
					player.last_name = request.POST['last_name']
					myfile = request.FILES['myfile']
					dir_storage = '/home/adil/ActionFi/UserData/media/profile_pics'
					fs = FileSystemStorage(location=dir_storage , base_url = dir_storage)
					filename = fs.save(myfile.name, myfile)
					player.profile_photo = filename
					player.age = request.POST['age']
					player.phone = request.POST['phone']
					player.save()
					return render(request,'Login_v10/welcome.html',{'player':player})
				else:
					return HttpResponse('alraedy exist')

class PlayerUpdation(View):
	def get(self, request, userid):
		player = Player.objects.filter(id=userid)
		return render(request,'Table_Responsive_v2/player_update_form.html',{'player':player})

	def post(self, request, userid):
		try:
			player = Player.objects.filter(id=userid)
		except:
			return HttpResponse("No user")
		if player:
			player.update(
				first_name = request.POST['last_name'],
				last_name = request.POST['last_name'],
				age = request.POST['age'],
				email = request.POST['email'],
				phone = request.POST['phone'],
				)
			return render(request,'Table_Responsive_v2/index.html',{'players':player})

def delete_palyer(request, userid):
	players = Player.objects.filter(id=userid).delete()

	return redirect('API to list players')





