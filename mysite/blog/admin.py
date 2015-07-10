from django.contrib import admin
from blog.models import Post, Section
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


class postAdmin(admin.ModelAdmin):

	fields = ['title', 'body', 'post_tags', 'author', 'created_on', 'section']

	list_display = ['title', 'author', 'created_on', 'section', 'return_tags']

	search_fields = ['title', '^section__section_name', 'post_tags']

	def queryset(self, request):
		qs = super(postAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		else:
			return qs.filter(author=request.user)


	#list_filter = ['author']

class sectionAdmin(admin.ModelAdmin):

	fields = ['section_name', 'enabled']

	list_display = ['section_name', 'enabled']

admin.site.register(Post, postAdmin)
admin.site.register(Section, sectionAdmin)