from django import template


register = template.Library()


@register.simple_tag
def highlight(request, value):
    if value in request.path:
        return 'active'
    else:
        return ''

