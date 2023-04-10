from django import template

register = template.Library()

@register.filter
def is_digit(value):
	if isinstance(value, (int, float)):
		return True
	else:
		return False
