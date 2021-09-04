from django.urls import path
from . import views

# # 함수형 view: url
# urlpatterns = [
#     path('', views.index, name="index"),
#     path('posts/', views.post_list, name="post-list"),
#     path('posts/new', views.post_create, name="post-create"),
#     path('posts/<int:post_id>/', views.post_detail, name="post-detail"),
#     path('posts/<int:post_id>/edit', views.post_update, name="post-update"),
#     path('posts/<int:post_id>/delete', views.post_delete, name="post-delete"),
# ]

# # 클래스형 view: url
# urlpatterns = [
#     path('', views.IndexRedirectView.as_view(), name="index"),
#     path('posts/', views.PostListView.as_view(), name="post-list"),
#     path('posts/new', views.PostCreateView.as_view(), name="post-create"),
#     path('posts/<int:post_id>/', views.PostDetailView.as_view(), name="post-detail"),
#     path('posts/<int:post_id>/edit', views.PostUpdateView.as_view(), name="post-update"),
#     path('posts/<int:post_id>/delete', views.PostDeleteView.as_view(), name="post-delete"),
# ]

# 클래스형 view: url (post_id -> pk로 변경)
urlpatterns = [
    path('', views.IndexRedirectView.as_view(), name="index"),
    path('posts/', views.PostListView.as_view(), name="post-list"),
    path('posts/new', views.PostCreateView.as_view(), name="post-create"),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('posts/<int:pk>/edit', views.PostUpdateView.as_view(), name="post-update"),
    path('posts/<int:pk>/delete', views.PostDeleteView.as_view(), name="post-delete"),
]