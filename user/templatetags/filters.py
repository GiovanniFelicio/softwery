from django import template
from datetime import datetime

register = template.Library()

@register.filter
def formatDateTime(date):
    return date