from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter


from . import views


router = DefaultRouter()

router.register(r'books', views.BookViewSet)

#book_list = views.BookViewSet.as_view({
    #'get': 'list',
    #'post': 'create'
#})

#book_detail = views.BookViewSet.as_view({
    #'get': 'retrieve',
    #'put': 'update',
    #'patch': 'partial_update',
    #'delete': 'destroy'
#})

urlpatterns = [
   #url(r'^books/$', views.book_list, name='book_list'),
   #url(r'^books/$', views.BookList.as_view(), name='book_list'),
   #url(r'^books/$', book_list, name='book-list'),
   #url(r'^books/(?P<pk>[0-9]+)$', book_detail, name='book-detail'),
   url(r'^', include(router.urls)),
]
