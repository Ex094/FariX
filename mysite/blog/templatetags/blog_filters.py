from django import template
from django.contrib.auth.models import Group


#Template Filters

register = template.Library()

@register.filter(name='check_perm')

def check_perm(user):
	if user.groups.filter(name="Administrator").exists():
		return True
	else:
		return False