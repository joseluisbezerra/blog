from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),

    path('management/', views.Management.as_view(), name='management'),

    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    path('about/', views.about, name='about'),
]
