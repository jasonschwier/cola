
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),

	path('projectschedule.html', views.projectschedule, name="projectschedule"),
	path('budgettable.html', views.budgettable, name = "budgettable"),
	path('aon.html', views.aon, name = "aon"),
	path('wbs.html', views.wbs, name = "wbs"),
	path('contact.html', views.contact, name = "contact"),
]