from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from convertor.views import PostListViewPage, PostDetailViewPage, \
                            PostCreateViewPage

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', PostListViewPage.as_view(), name='post-home'),
    url(r'list', PostListViewPage.as_view(), name='post-list'),
    url(r'create', PostCreateViewPage.as_view(), name='post-create'),
    url(r'detail/(?P<slug>[\w-]+)/$', PostDetailViewPage.as_view(), 
        name='post-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)