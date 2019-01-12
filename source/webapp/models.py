from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_inf', verbose_name='Пользователь')
    friends = models.ManyToManyField(User, max_length=300, blank=True, verbose_name='Друзья')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    avatar = models.ImageField(verbose_name='Фотография', null=True, blank=True)

    def __str__(self):
        return self.user


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=1000, verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.PROTECT, max_length=200, verbose_name='Автор')

    def __str__(self):
        return '%s %s' % (self.title, self.author)
