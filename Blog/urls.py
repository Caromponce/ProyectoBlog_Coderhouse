from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


#path(route, view, kwargs=None, name=None)
urlpatterns = [
    path('', views.Articles.as_view(), name='blog'),
    path('createArticle', views.CreateArticle.as_view()),#Esta línea dice que para cada URL que empieza con createArticle Django encontrará su correspondiente view.
    path('article/<int:pk>', views.ReadArticle.as_view()),
    path('editArticle/<int:pk>', views.EditArticle.as_view())
]


