from django.shortcuts import render

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
	return render(request, "contact.html", {})