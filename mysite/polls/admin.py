from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInLine(admin.TabularInline):

	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):

	fieldsets = [
	(None, {'fields': ['question']}),
	('Date Information', {'fields': ['pub_date'], 'classes': ['collaspe']}),
	]

	inlines = [ChoiceInLine]

	list_display = ('question', 'pub_date', 'was_published_recently')

	list_filter = ['pub_date']

	search_fields = ['question', 'choice__choice_text']

admin.site.register(Poll, PollAdmin)