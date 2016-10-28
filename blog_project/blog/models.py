# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


# 用户模型(可采用继承的方式去扩展用户信息(本例中使用)或者使用关联的方式去扩展)
class BlogUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', default='avatar/defautl.png', verbose_name='用户头像')
    qq = models.CharField(max_length=20, verbose_name='qq')
    mobile = models.CharField(max_length=20, verbose_name='手机')
    url = models.URLField(max_length=100, verbose_name='个人网页地址')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=10, verbose_name='分类名称')
    index = models.IntegerField(default=99, verbose_name='分类的排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 文章model的Manager类
class ArcicleManager(models.Manager):
    def get_distinct_date(self):
        ret_date_list = []

        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y-%m')
            if date not in ret_date_list:
                ret_date_list.append(date)
        return ret_date_list


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name='文章名称')
    desc = models.CharField(max_length=20, verbose_name='文章描述')
    content = models.CharField(max_length=200, null=True, verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')  # auto_now_add是自动增加时间的吗
    user = models.ForeignKey(BlogUser, verbose_name='用户')
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name='分类')  # 难道默认都是要求非空的吗
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    objects = ArcicleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']  # 减号是倒序输出！时间倒序就是最大的时间最前面

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    username = models.CharField(max_length=10, verbose_name='用户名')
    emain = models.EmailField(max_length=20, verbose_name='用户邮箱')
    url = models.URLField(max_length=100, verbose_name='个人网页地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(BlogUser, verbose_name='用户')
    article = models.ForeignKey(Article, verbose_name='文章')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')  # 这个字段有点不清楚啊

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content


class Links(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    description = models.CharField(max_length=50, verbose_name='友情链接描述')
    callback_url = models.URLField(verbose_name='url地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=99, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Ad(models.Model):
    title = models.CharField(max_length=20, verbose_name='广告标题')
    description = models.CharField(max_length=50, verbose_name='广告描述')
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')
    callback_url = models.URLField(verbose_name='回调url')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=99, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = u'广告'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
