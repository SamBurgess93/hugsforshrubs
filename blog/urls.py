from django.urls import path
from blog.views import (
    all_blog_posts,
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
)


urlpatterns = [
    path('', all_blog_posts, name="blog"),
    path('create/', create_blog_view, name="create"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('edit_blog/<int:blog_id>', edit_blog_view, name="edit"),
]