from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from articles.forms import ArticleForm
from articles.models import Article
from blog.models import Blog


class HomeView(ListView):

    model = Article
    template_name = 'home/detail.html'

    def get_queryset(self):
        return super().get_queryset().filter(ative=True).order_by('-posted_on')[:12]

class ArticleDetailView(View):

    def get(self, request, username, pk):

    try:
        user_id = User.objects.get(username=username).id
    except User.DoesNotExist:
        return HttpResponse('No encontramos ningún artículo con este usuario', status=404)

    try:
        blog_id = Blog.objects.get(owner=user_id).id
    except  Blog.DoesNotExist:
        return HttpResponse('No hay ningún artículo asociado a este blog', status=404)

    try:
        article = Article.object.filter(blog=blog_id).get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse('No encontramos el artículo solicitado', status=404)

    context = {'article': article}

    return render(request, 'articles/detail.html', context)


class UserView(View):

    def get(self, request, username, pk):

    try:
        author = Article.objects.get(username=username, pk=pk)
    except Article.DoesNotExist:
        return HttpResponse('No hemos encontrado ningún artículo asociado a este usuario', status=404)

    context = {'author': author}

    return render(request, 'user_articles_detail.html', context)


@method_decorator(login_required, name='dispatch')
class NewArticleView(View):

    def get(self, request):

        form = ArticleForm()

        context = {'form': form}

        return render(request, 'new_article.html', context)

    def post(self, request):

        article = Article()
        article.author = request.user
        form = ArticleForm(request.POST, request.FILES, instance=article)

        if form.is_valid():
            article = form.save()

        return redirect('user_articles_detail.html', self.id)