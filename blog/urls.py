from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('edit/<int:pk>/', ArticleEditView.as_view(), name='article_edit'),
    path('new/', ArticleCreateView.as_view(), name='article_create'),

]
