from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

def projectschedule(request):
	return render(request, "projectschedule.html", {})

def budgettable(request):
	return render(request, "budgettable.html", {})


def aon(request):
	return render(request, "aon.html", {})

def wbs(request):
	return render(request, "wbs.html", {})

def contact(request):
	if request.method == "POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		
		send_mail(
			message_name,   #subject
			message,	# message
			message_email,	# from email
			['jasonschwier486@gmail.com'],	# to email
			fail_silently=True, 
			)

		return render(request, 'contact.html', {'message_name':message_name})
	else:
		#return the page
		return render(request, 'contact.html', {})