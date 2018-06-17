
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from articles.views import NewArticleView, ArticleDetailView, HomeView, UserView
from blog.views import BlogsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/<str:username>/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('admin/', admin.site.urls),
    path('blogs', BlogsView.as_view(), name='blogs'),
    path('blog/<str:username>', UserView.as_view(), name='user_blog'),
    path('article/new', NewArticleView.as_view(), name='new_article'),
    patch('blog/new', NewBlogView.as_view(), name='new_blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
