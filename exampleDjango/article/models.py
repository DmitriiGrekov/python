from django.db import models

# Create your models here.



class Article(models.Model):

    title = models.CharField(max_length = 60, verbose_name = 'Заголовок')
    content = models.TextField(verbose_name = 'Текст статьи')
    date = models.DateTimeField(auto_now_add = True)


    class Meta:

        verbose_name_plural = 'Статьи'

        verbose_name = 'Статья'

    def __str__(self):
        return self.title

