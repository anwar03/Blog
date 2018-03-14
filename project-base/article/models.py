from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.text import Truncator
from django.conf import settings



class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'users', on_delete = models.CASCADE, blank=True)
    title = models.CharField(max_length = 255)
    article = models.CharField(max_length = 5000)
    created_at = models.DateTimeField(auto_now_add = timezone.now())
    updated_at = models.DateTimeField(auto_now_add = True)
    view = models.PositiveIntegerField(default = 0)

    class Meta:
        ordering = ('-created_at', )
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        truncated_article = Truncator(self.title)
        return truncated_article.chars(100)

    def get_last_three_comments(self):
        return self.comments.order_by('-created_at')[:5]


class Comment(models.Model):
    comment = models.CharField(max_length=1000, blank=False)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=timezone.now())
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at', )
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        truncated_comment = Truncator(self.comment)
        return truncated_comment.chars(100)
    

class Reply(models.Model):
    reply = models.CharField(max_length=1000, blank=False)
    comment = models.ForeignKey(Comment, related_name='replys', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='replys', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=timezone.now())
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at', )


    def __str__(self):
        truncated_reply = Truncator(self.reply)
        return truncated_reply.chars(100)
    

    