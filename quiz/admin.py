from django.contrib import admin
from .models import Questions, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Number of choices displayed by default in the Questions admin form

class QuestionsAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Questions, QuestionsAdmin)
