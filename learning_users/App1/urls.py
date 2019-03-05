from django.urls import path
from App1 import views


#Template URLS!

app_name= 'App1'

urlpatterns=[
	path('login/',views.user_login,name='user_login'),
	path('register/',views.register,name='register'),
]