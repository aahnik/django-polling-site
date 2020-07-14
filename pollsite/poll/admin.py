from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['featured']}),
        ('Question Information', {'fields': ['title', 'desc']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('title', 'recent', 'pub_date', 'participants')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Question, QuestionAdmin)
