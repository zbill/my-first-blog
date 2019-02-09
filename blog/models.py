from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # 定义外键时需要on_delete,cascade是级联删除
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)  # blank针对表单，可以不填写内容，null针对数据库，字段可以为空（新建model对象时不会报错）

    def pulish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
