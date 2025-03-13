from django import template

register = template.Library()

@register.filter
def get_base_of_path(value, delimiter='/'):
    """Split the value by the delimiter"""
    return value.split(delimiter)[1]