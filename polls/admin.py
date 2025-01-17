from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Statment', {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    # fields = ['pub_date', 'question_text']
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
