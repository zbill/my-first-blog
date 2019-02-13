from django.urls import path
from . import views

urlpatterns = [
    # 首页
    path('', views.post_list, name='post_list'),
    # 文章详情页
    path('post/<post_id>', views.post_detail, name='post_detail'),
    # 新增页
    path('new', views.new_post, name='new_post'),  # 暂时还不清楚为什么不能用post/new
    # 编辑页
    path('post/<post_id>/edit', views.edit_post, name='edit_post')
]