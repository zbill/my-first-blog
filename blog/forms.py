# 表单

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        # 定义将用哪个模型常见表单 Post
        model = Post
        # 定义哪些字段出现在表单里，title和text，author等应自动识别
        fields = ('title', 'text',)

