from django import template
from softwery.utils import stringUtil

register = template.Library()

@register.filter
def cut(value: str, length: int):
    return stringUtil.cut(value, length)
