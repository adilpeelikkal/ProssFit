
from django.contrib import admin
from django.urls import path, include
import userprofile.views
import players.views
import guest.views

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 


urlpatterns = [
    path('admin/', admin.site.urls),
    # admin related urls
    path('', userprofile.views.GuestSection.as_view(), name='Api to load guest section'),
    path('users/', userprofile.views.Registration.as_view(), name='users'),
    path('userslogin/', userprofile.views.UserLogin.as_view(), name='userslogin'),
    path('user/signup', userprofile.views.UserSignup.as_view(), name='User signup page'),
    path('userregister/', userprofile.views.UserRegister.as_view(), name='userregister'),
    path('forgotpassword/', userprofile.views.ForgotPassword.as_view(), name='forgotpassword'),
    path('confirmpassword/', userprofile.views.ConfirmPassword.as_view(), name='confirmpassword'),

    # players related urls
    path('players/view/',players.views.PlayersDetails.as_view(),name= 'API to list players'),
    path('players/add/',players.views.PlayersRegistration.as_view(),name= 'API to add players'),
    path('players/details/<int:userid>/',players.views.PlayerUpdation.as_view(),name= 'API for View and Update player'),
    path('players/details/delete/<int:userid>/',players.views.delete_palyer,name= 'API for Delete player'),

    # guest related urls
    path('about/us/',guest.views.AboutUs,name= 'API to load about-us'),
    path('schedule/',guest.views.Schedule,name= 'API to load schedule'),
    path('gallery/',guest.views.Gallery,name= 'API to load gallery'),
    path('contacts/',guest.views.Contact,name= 'API to load contact'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)