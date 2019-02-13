from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')  # lte小于等于
    return render(request, 'blog/post_list.html', {'posts': posts})  # 接受request参数，用render渲染模板中的blog/xxx.html模板


def post_detail(request, post_id):
    this_post = get_object_or_404(Post, id=post_id)  # 如果可以找到对应id则返回对象，否则报404错误
    return render(request, 'blog/post_detail.html', {'post_detail': this_post})


def new_post(request):
    if request.method == "POST":  # 非首次进入
        edit_form = PostForm(request.POST)
        if edit_form.is_valid():
            post = edit_form.save(commit=False)  # 暂不存，还需要添加作者信息author
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:  # 首次进入页面
        edit_form = PostForm()
    return render(request, 'blog/edit_post.html', {'edit_form': edit_form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # 同detail页面验证id一致
    if request.method == "POST":
        edit_form = PostForm(request.POST, instance=post)
        if edit_form.is_valid():
            post = edit_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post_id)
    else:
        edit_form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'edit_form': edit_form})

