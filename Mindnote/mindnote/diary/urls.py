from django.urls import path, include
from . import views

# # 함수형 view: url
# urlpatterns = [
#     path('', views.index, name="index"),
#     path('diary/', views.page_list, name="page-list"),
#     path('diary/info/', views.info, name="info"),
#     path('diary/write/', views.page_create, name="page-create"),
#     path('diary/page/<int:page_id>/', views.page_detail, name="page-detail"),
#     path('diary/page/<int:page_id>/edit/', views.page_update, name="page-update"),
#     path('diary/page/<int:page_id>/delete/', views.page_delete, name="page-delete"),
# ]

# # 클래스형 view: url
# urlpatterns = [
#     path('', views.index, name="index"),
#     path('diary/', views.PageListView.as_view(), name="page-list"),
#     path('diary/info/', views.info, name="info"),
#     path('diary/write/', views.PageCreateView.as_view(), name="page-create"),
#     path('diary/page/<int:page_id>/', views.PageDetailView.as_view(), name="page-detail"),
#     path('diary/page/<int:page_id>/edit/', views.PageUpdateView.as_view(), name="page-update"),
#     path('diary/page/<int:page_id>/delete/', views.PageDeleteView.as_view(), name="page-delete"),
# ]

# 클래스형 view: url (post_id -> pk로 변경)
urlpatterns = [
    path('', views.index, name="index"),
    path('diary/', views.PageListView.as_view(), name="page-list"),
    path('diary/info/', views.info, name="info"),
    path('diary/write/', views.PageCreateView.as_view(), name="page-create"),
    path('diary/page/<int:pk>/', views.PageDetailView.as_view(), name="page-detail"),
    path('diary/page/<int:pk>/edit/', views.PageUpdateView.as_view(), name="page-update"),
    path('diary/page/<int:pk>/delete/', views.PageDeleteView.as_view(), name="page-delete"),
]