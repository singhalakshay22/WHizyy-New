from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import RegistrationForm,AccountAuthenticationForm
from django.contrib.auth.decorators import login_required
from users.models import Account,UserFollowing
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
def blog_view(request):
	return render(request,'recipes.html')

@login_required()
def userpage_view(request,username):



	user=Account.objects.get(username=username)

	followers_count=user.followers.all().count()
	
	is_follower=False	

	for element in user.followers.all():
		if request.user==element.user_id:
			is_follower=True


	context={
	'followers_count':followers_count,
	'is_follower':is_follower,
	'profile_user': user,
	}	

	return render(request,'userpage.html',context)

@login_required()
def follow_view(request,username):



	user=Account.objects.get(username=username)
	print(user)

	UserFollowing.objects.create(user_id=request.user,
                             following_user_id=user)
	
	return redirect('userpage', username=username)

@login_required()
def unfollow_view(request,username):



	user=Account.objects.get(username=username)
	

	element=UserFollowing.objects.get(user_id=request.user,
                             following_user_id=user)
	element.delete()
	
	return redirect('userpage', username=username)



