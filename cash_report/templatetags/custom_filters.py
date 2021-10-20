from django import template

register = template.Library()


def show_only_nums(value, num):
    value_str = str(value)
    return value_str[:int(num)]


register.filter('show_only_nums', show_only_nums)