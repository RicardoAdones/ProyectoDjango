from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def list(request):
    #obtener articulos
    articles = Article.objects.filter(public=True)
    #Paginar articulos
    paginator = Paginator(articles, 2)

    #obtener numero de pagina

    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_articles,
    })
@login_required(login_url='login')
def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    #articles = Article.objects.filter(categories=category_id)    #esta es otra forma de obtener los articulos de las diferentes categorias (la forma que dejamos es la comentada en category.html)

    return render(request, 'categories/category.html', {
        'category' : category,
        #'articles' : articles,

    })
@login_required(login_url='login')
def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html', {
        'article': article,
    })

@login_required(login_url='login')
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            form.save_m2m()  # Guarda las relaciones many-to-many (categorías)
            messages.success(request, '¡Artículo creado correctamente!')
            return redirect('article', article.id)
    else:
        form = ArticleForm()
    
    return render(request, 'articles/create.html', {
        'form': form,
        'title': 'Crear Artículo',
    })