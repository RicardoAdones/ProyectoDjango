from blog.models import Category, Article

def get_categories(request):

    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name') #.filter(id__in=categories_in_use) una subconsulta

    return {
        'categories': categories,
        'ids': categories_in_use,
    }

def get_articles(request):

    articles_in_use = Artcile.objects.filter(public=True).value_list('')