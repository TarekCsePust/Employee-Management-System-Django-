from django.shortcuts import render,redirect,HttpResponse,Http404,get_object_or_404
from .forms import RegisterForm,LoginForm,ProfileUpadteForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .token import activation_token
from EmployeeManagement.task import send_feedback_email_task
from django.contrib import messages
from django.contrib.auth import get_user_model,authenticate,login,logout
User = get_user_model()
# Create your views here.


def login_user(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		user = request.POST.get("username")
		password = request.POST.get("password")
		auth = authenticate(request, username=user, password=password)
		print(auth.is_active)
		if auth is not None:
			if auth.is_active:
				login(request,auth)
			
			return redirect("employee:list")
		else:
			return redirect("account:login")
        
            #messages.add_message(request, messages.ERROR, "Username or password mismatch.")
	return render(request,"login.html",{"form":form})

def Registration(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.is_active = False
		instance.save()
		site = get_current_site(request)
		mail_subject = "Confirmation message for blog"
		message = render_to_string('confirm_email.html',{
                "user":instance,
                "domain":site.domain,
                "uid":instance.id,
                "token":activation_token.make_token(instance)
            })
		to_email = form.cleaned_data.get("email")
		to_list = [to_email]
		from_email = settings.EMAIL_HOST_USER
		send_feedback_email_task.delay(mail_subject,message,from_email,to_list)
		#send_mail(mail_subject,message,from_email,to_list,fail_silently=True)
		return redirect("account:login")
		return HttpResponse("<h2>thank you for your registration.A confirmation link was sent to your email</h2>")   
        #return render(request,'register.html',{"form":form})
		print("save info")
		#return redirect("account:registration")
	page = "Create Account"
	return render(request,"register.html",{"form":form,"page":page})



def getProfile(request):
	if request.user.is_authenticated:
		user = get_object_or_404(User,pk=request.user.id)
		return render(request,"profile.html",{"user":user})
	return redirect("account:login")




def profileUpdate(request):
	
	if request.user.is_authenticated:
		user = get_object_or_404(User,pk=request.user.id)

		if request.POST:
			user.first_name = request.POST.get("first_name")
			user.last_name =request.POST.get("last_name")
			user.email = request.POST.get("email")
			user.save()
			return redirect("account:profile")
		
		return render(request,"profile_update.html",{"user":user})
	return redirect("account:login")

def activate(request,uid,token):
    try:
        user = get_object_or_404(User,pk=uid)
    except:
        raise Http404("No user found")
    if user is not None and activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        return HttpResponse("<h2>Account is now activeted .you can login now</h2>")
    else:
        return HttpResponse("Invalid activation link")
        
def logout_user(request):
	logout(request)
	return redirect("account:login")
