from dateutil.parser import parse
from datetime import timedelta
from django.shortcuts import render
from .models import Article
from .filters import ArticleFilter


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def person_list(request):
    template_name = 'core/person_list.html'
    return render(request, template_name)


def article_list(request):
    template_name = 'core/article_list.html'
    object_list = Article.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Converte em data e adiciona um dia.
        end_date = parse(end_date) + timedelta(1)
        object_list = object_list.filter(
            published_date__range=[start_date, end_date]
        )

    context = {'object_list': object_list}
    return render(request, template_name, context)


def article_filter_list(request):
    template_name = 'core/article_filters_list.html'
    object_list = Article.objects.all()
    article_list = ArticleFilter(request.GET, queryset=object_list)

    context = {
        'object_list': object_list,
        'filter': article_list
    }
    return render(request, template_name, context)
