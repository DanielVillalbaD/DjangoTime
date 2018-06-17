from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from blog.form import BlogForm
from blog.models import Blog


class BlogsView(View):

    def get(self, request):

        try:
            blogs = Blog.objects.filter(active=True).order_by('-create_on')
        except Blog.DoesNotExist:
            return HttpResponse('No hemos encontrado ningún blog', status=404)

        context = {'blogs': blogs}

        return render(request, 'blogs/list.html', context)


    @method_decorator(login_required, name='dispatch')
    class NewBlogView(View):

        def get(self, request):

            form = BlogForm()

            context = {'form': form}
            return render(request, 'blogs/form.html', context)

        def post(self, request):

            blog = Blog()

            try:
                blog.owner = User.objects.get(username=request.user)
            except User.DoesNotExist:
                return HttpResponse('Usuario inválido', status=404)

            form = BlogForm(request.POST, request.FILES, instance=blog)

            if form.is_valid():
                form.save()
                messages.sucess(request, 'Blog creado correctamente')

            context = {'form': form}
            return render(request, 'blogs/form.html', context)