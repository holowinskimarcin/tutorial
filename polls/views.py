from django.shortcuts import render
from polls.models import Poll
# Create your views here.

def widok(request):
	data = "Dowolny tekst"
	ques = Poll.objects.get(id = 1)
	return render(request, "pierwszy_projekt.html", {"dowolna":data, "pytanie":ques})