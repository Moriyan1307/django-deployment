from django import template

register = template.Library()
@ register.filter(name='cut')
def cut(value,arg):
    """
    this cuts and which you will provide in args
    """
    return value.replace(arg,'')

