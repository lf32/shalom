from django.contrib import admin
from django.urls import path

from social import views

urlpatterns = [
        path('', views.index_view, name="index_view"),
        path('<int:book>', views.book_view, name="book_view"),
        path('<int:book>/<int:chapter>', views.chapter_view, name="chapter_view"),
]
