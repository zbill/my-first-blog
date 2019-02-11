from django.shortcuts import render

# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {})
    # 接受request参数，用render渲染模板中的blog/xxx.html模板
