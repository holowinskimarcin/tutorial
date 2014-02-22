from django.shortcuts import render
from polls.models import Question
# Create your views here.

def widok(request):
	data = "Dowolny tekst"
	ques = Question.objects.get(id = 1)
	return render(request, "pierwszy_projekt.html", {"dowolna":data, "pytanie":ques})