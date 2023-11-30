from django import template
import musicians.views as views
from musicians.models import Categories

register = template.Library()


@register.inclusion_tag('musicians/list_categories.html')
def show_categories(cat_selected=0):
    cats = Categories.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
