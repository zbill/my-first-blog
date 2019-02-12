from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<post_id>', views.post_detail, name='post_detail')
]