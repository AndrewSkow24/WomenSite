from django import template
import women.views as view

# регистрация собственных шаблонных тегов
register = template.Library()

@register.simple_tag()
def get_categories():
    return view.cats_db

@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = view.cats_db
    return {
        "cats": cats,
        'cat_selected': cat_selected,
    }