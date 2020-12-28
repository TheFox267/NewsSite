# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name='название')
    slug = models.SlugField(max_length=120, unique=True, verbose_name='url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'
        ordering = ['title']


class News(models.Model):
    slug = models.SlugField(max_length=150, unique=True, verbose_name='url')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='автор')
    title = models.CharField(verbose_name='заголовок', max_length=150)
    content = models.TextField(verbose_name='контент')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='постер', default='photos/default.svg')
    posted = models.BooleanField(verbose_name='размещено?', default=True)
    views = models.IntegerField(default=0, verbose_name='количество просмотров')
    likes = models.IntegerField(default=0, verbose_name='количество лайков')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='news')
    tags = models.ManyToManyField(Tag, blank=True, related_name='news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-create_date']
