from django.shortcuts import render

# Create your views here.

def widok(request):
	return render(request, "pierwszy_projekt.html")