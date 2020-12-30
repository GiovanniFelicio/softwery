from django import template

import sys
sys.path.append('...')

from utils import stringUtil

register = template.Library()

@register.filter
def cut(value: str, length: int):
    return stringUtil.cut(value, length)
