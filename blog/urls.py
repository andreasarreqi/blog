from . import views
from django.urls import path

urlpatterns = [
    path('', views.MusicianList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post', views.AddPost.as_view(), name='add_post'),
    path('shared_posts', views.SharedPostsByUsers.as_view(), name='shared_posts'),  # noqa: E501
    path('<slug:slug>/update', views.UpdatePost.as_view(), name='update_post'),  # noqa: E501
    path('<slug:slug>/delete_post', views.DeletePost.as_view(), name='delete_post'),  # noqa: E501
]
