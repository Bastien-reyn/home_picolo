from django import template

register = template.Library()


def role_replace(value):
    role = ['', 'Normal', 'On a soif', 'Hot']
    return role[value]


def role_color(value):
    role = ['', '', 'bg-warning', 'bg-danger']
    return role[value]


register.filter('role_replace', role_replace)
register.filter('role_color', role_color)
