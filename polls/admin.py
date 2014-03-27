from django.contrib import admin
import models 
# Register your models here.

class PollsAdmin(admin.ModelAdmin):
	list_display = ("id", "question")

admin.site.register(models.Poll, PollsAdmin)	