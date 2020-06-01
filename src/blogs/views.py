from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import RegistrationForm,AccountAuthenticationForm
from users.models import Account
# Create your views here.
def home_view(request,*args,**kwargs):

	
	context = {}
	#FOR PRINTING THE LOGGED IN USERS NAME IN THE NAVBAR
	# print_username = False
	# if request.user in Account.objects.all():
	# 	print_username = True
	# 	context['user']=request.user


	# context['print_username'] = print_username
	
	#FOR REGISTRATION
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form
	else: #GET request
		form = RegistrationForm()
		context['registration_form'] = form



	user = request.user
	 # if user.is_authenticated:
	 # 	return redirect("home")

	if request.POST:
		form1 = AccountAuthenticationForm(request.POST)
		if form1.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form1 = AccountAuthenticationForm()

	context['login_form'] = form1
	

	return render(request, 'home.html', context)


def logout_view(request):
	logout(request)
	return redirect ('home')