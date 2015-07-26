from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.views.generic import TemplateView
# Create your views here.

class SplashView(TemplateView):
	template_name = "index.html"

	

>>>>>>> a3cae2367010b0b071e5943437dc8e44353371cc
