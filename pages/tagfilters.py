from django import template

register = template.Library()


@register.filter
def concatenate(s1, s2):
    return "{} {}".format(s1, s2)
