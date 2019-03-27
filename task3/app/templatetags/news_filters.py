from django import template

from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    date_now = datetime.timestamp(datetime.now())
    delta = date_now - value
    if delta < 600:
        return "Только что"
    elif 600 <= delta < 86400:
        hours_ago = round(delta / 3600)
        return f"{hours_ago} часов назад"
    elif delta >= 86400:
        post_date = datetime.utcfromtimestamp(value).date()
        return post_date.strftime('%Y-%m-%d')


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value):
    if value < -5:
        return "все плохо"
    elif -5 <= value <= 5:
        return "нейтрально"
    elif value > 5:
        return "хорошо"


@register.filter
def format_num_comments(value):
    if value == 0:
        return "Оставьте комментарий"
    elif 0 < value <= 50:
        return value
    else:
        return "50+"


@register.filter
def format_selftext(value, count):
    if value:
        text_init = value.split()
        text_res1 = " ".join(text_init[:count])
        text_res2 = " ".join(text_init[-count:])
        return f"{text_res1} ... {text_res2}"
    else:
        return ""
