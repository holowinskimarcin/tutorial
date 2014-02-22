from django.contrib import admin
import models 
# Register your models here.

class PollsAdmin(admin.ModelAdmin):
	list_display = ("id", "question_text")

admin.site.register(models.Question, PollsAdmin)	