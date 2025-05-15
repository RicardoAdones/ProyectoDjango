from django.urls import path
from . import views


urlpatterns = [
    path('articulos/', views.list, name='list_articles'),
    path('articulo/crear/', views.create_article, name='create_article'),
    path('categorias/crear/', views.create_category_ajax, name='create_category_ajax'),
    path('categorias/<int:category_id>', views.category, name='category'),
    path('articulo/<int:article_id>', views.article, name='article'),
    
]
