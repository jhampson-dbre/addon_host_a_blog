from urllib.parse import urlparse, urlunparse
from blog.models import BlogCategory as Category, Tag
from django.template import Library, loader
from django.http import QueryDict


register = Library()


@register.inclusion_tag('blog/components/tags_list.html',
                        takes_context=True)
def tags_list(context):
    tags = Tag.objects.all()
    return {
        'request': context['request'],
        'blog_page': context['blog_page'],
        'tags': tags
    }


@register.inclusion_tag('blog/components/categories_list.html',
                        takes_context=True)
def categories_list(context):
    categories = Category.objects.all()
    return {
        'request': context['request'],
        'blog_page': context['blog_page'],
        'categories': categories
    }


@register.inclusion_tag("blog/components/post_categories_list.html", takes_context=True)
def post_categories_list(context):
    page = context["page"]
    post_categories = page.categories.all()
    return {
        "request": context["request"],
        "post_categories": post_categories,
    }


@register.inclusion_tag("blog/components/post_tags_list.html", takes_context=True)
def post_tags_list(context):
    page = context["page"]
    post_tags = page.tags.all()
    return {
        "request": context["request"],
        "post_tags": post_tags,
    }


@register.simple_tag
def url_replace(request, **kwargs):
    """
    This tag can help us replace or add querystring
    TO replace the page field in URL
    {% url_replace request page=page_num %}
    """
    (scheme, netloc, path, params, query,
     fragment) = urlparse(request.get_full_path())
    query_dict = QueryDict(query, mutable=True)
    for key, value in kwargs.items():
        query_dict[key] = value
    query = query_dict.urlencode()
    return urlunparse((scheme, netloc, path, params, query, fragment))
