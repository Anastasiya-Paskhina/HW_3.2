from django import template


register = template.Library()


@register.filter
def color_range(value):
    if value == '-':
        return ''
    else:
        if float(value) < 0:
            return '#79e86a'
        elif 1 <= float(value) <= 2:
            return '#ffa0a0'
        elif 2 < float(value) <= 5:
            return '#f96161'
        elif float(value) > 5:
            return '#ff2b2b'
        else:
            return ''

