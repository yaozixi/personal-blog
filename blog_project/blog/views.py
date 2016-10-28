# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from models import Article, Comment, Tag, Category
from django.core.paginator import Paginator
import logging
from django.db.models import Count


logger = logging.getLogger('blog.views')


def global_setting(request):
    # 站点基本信息
    BLOG_TITLE = settings.BLOG_TITLE
    BLOG_SIGNATURE = settings.BLOG_SIGNATURE
    BLOG_FOOTER = settings.BLOG_FOOTER
    # 分类信息获取（导航数据）
    category_list = Category.objects.all()[:6]
    # 文章归档数据
    archive_list = Article.objects.get_distinct_date()
    # 年份月份获取
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)
    # 广告数据（同学们自己完成）
    # 标签云数据（同学们自己完成）
    # 友情链接数据（同学们自己完成）
    # 站长推荐文章
    article_recomment_list = Article.objects.filter(is_recommend=True)
    # 文章浏览排行榜数据
    article_click_list = Article.objects.all().order_by('-click_count')
    # 评论排行
    comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]
    return locals()


def get_paginate(article_list, page):
    paginator = Paginator(article_list, 2)
    article_list = paginator.page(page)

    return article_list


def index(request):
    try:
        # 文章
        article_list = Article.objects.all()
        page = request.GET.get('page', 1)
        # 文章分页
        article_list = get_paginate(article_list, page)

        print type(article_list[0]), type(article_list)
    except Exception as e:
        print e
        logger.error(e)

    return render(request, 'index.html', locals())


def archive(request):
    try:
        page = request.GET.get('page', 1)
        year = request.GET.get('year')
        month = request.GET.get('month')

        # 归档列表
        archive_list = Article.objects.get_distinct_date()
        print type(archive_list[0])
        # 文章
        article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
        article_list = get_paginate(article_list, page)
    except Exception as e:
        print e
        logger.error(e)

    return render(request, 'index.html', locals())


def comment_order(request):
    try:
        page = request.GET.get('page', 1)

        # 文章
        comment_list = Comment.objects.values('article').annotate(cnt=Count('article')).order_by('-cnt')
        article_list = [Article.objects.get(pk=comment['article']) for comment in comment_list]
        article_list = get_paginate(article_list, page)
        return render(request, 'index.html', locals())
    except Exception as e:
        logger.error(e)
        return render(request, 'failure.html', locals())
