from django.conf.urls import handler404
from django.urls import path, re_path, register_converter
from women import views

from . import converters
from .views import page_not_found

register_converter(converters.FourDigitConverter, "year4")

'''
В пути 'cats/<int:cat_id>/' записан параметр cat_id, который имеет тип 
int. Этот тип в маршрутах называется конвертером. И указанный путь 
будет соответствовать комбинациям URL c фрагментом cats/число/.
Далее в функции представления categories можно использовать этот параметр
'''

'''
Помимо конвертора int в Django можно использовать и другие: 

- str - любая непустая строка, исключающая символ /
- int - любое положительное целое число, включающее 0
- slug - латиница, ASCII-символы, цифры, дефисы, подчёркивания
- uuid - цифры, малые латинские символы ASCII, дефис 
- path - любая не пустая строка, включая символ /
 

'''

handler404 = page_not_found

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<int:cat_id>', views.show_category, name='category')
]