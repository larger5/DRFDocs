from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from booktest.views import BooksListViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

# 配置 url
router = DefaultRouter()
router.register(r'books',BooksListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'docs/', include_docs_urls(title="后台接口")),
    url(r'^', include(router.urls)),
]
