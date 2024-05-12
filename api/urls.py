from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.IndexSerializer.as_view()),
    path('category-book/<str:code>/', views.CategoryBookSerializer.as_view()),
    path('author-list/', views.AuthorListSerializer.as_view()),
    path('author-detail/<str:code>/', views.AuthorDetailSerializer.as_view()),
    path('book-list/', views.BookListSerializer.as_view()),
    path('book-detail/<str:code>/', views.BookDetailSerializer.as_view()),
]