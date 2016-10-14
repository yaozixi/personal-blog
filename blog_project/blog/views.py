# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from models import Article
from django.core.paginator import Paginator
import logging

logger = logging.getLogger('blog.views')


def global_setting(request):
    # 站点基本信息
    BLOG_TITLE = settings.BLOG_TITLE
    BLOG_SIGNATURE = settings.BLOG_SIGNATURE
    BLOG_FOOTER = settings.BLOG_FOOTER
    # 分类信息获取（导航数据）
    # category_list = Category.objects.all()[:6]
    # 文章归档数据
    # archive_list = Article.objects.distinct_date()
    # 广告数据（同学们自己完成）
    # 标签云数据（同学们自己完成）
    # 友情链接数据（同学们自己完成）
    # 文章排行榜数据（按浏览量和站长推荐的功能同学们自己完成）
    # 评论排行
    # comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    # article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]
    return locals()


def get_paginate(article_list, page):
    paginator = Paginator(article_list, 2)
    article_list = paginator.page(page)

    return article_list


def index(request):
    BLOG_TITLE = settings.BLOG_TITLE

    try:
        a = request.GET.get('page')
        b = request.GET['page']
        c = request.GET.page
        print '----------'
        print a, b, c


        # 归档列表
        archive_list = Article.objects.get_distinct_date()

        # 文章
        article_list = Article.objects.all()
        paginator = Paginator(article_list, 2)
        page = request.GET.get('page', 1)
        article_list = paginator.page(page)
    except Exception as e:
        print e
        logger.error(e)

    return render(request, 'index.html', locals())


def archive(request):
    try:
        request.GET.year
        page = request.GET.get('page', 1)
        year = request.GET.get('year')
        month = request.GET.get('month')
        # 归档列表
        archive_list = Article.objects.get_distinct_date()
        # 文章
        article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
        article_list = get_paginate(article_list, page)
    except Exception as e:
        print e
        logger.error(e)

    return render(request, 'index.html', locals())
