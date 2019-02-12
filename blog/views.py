from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  # lte小于等于
    return render(request, 'blog/post_list.html', {'posts': posts})  # 接受request参数，用render渲染模板中的blog/xxx.html模板

