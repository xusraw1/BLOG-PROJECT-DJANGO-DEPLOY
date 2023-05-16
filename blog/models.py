from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=300)
    text = RichTextField()
    photo = models.ImageField(upload_to='article_photos/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    comment = models.CharField(max_length=300)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment[:30]

    def get_absolute_url(self):
        return reverse('articles')
