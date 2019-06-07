from django.db import models
from django.template.defaultfilters import truncatechars


class Category(models.Model):
    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "categories"


class Post(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    categories = models.ManyToManyField('Category', related_name = 'posts')
    #slug = slugify(title)

    def __str__(self):
        return self.title

    @property
    def short_description(self):
        return truncatechars(self.body, 100)
    
    class Meta:
        verbose_name_plural = "posts"


class Comment(models.Model):
    author = models.CharField(max_length = 60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    
    def __str__(self):
        return '{} {} {} -> {}'.format(self.post, self.created_on.strftime("%b %d %Y %H:%M"), self.author, self.body)

    @property
    def short_description(self):
        return truncatechars(self.body, 100)

    class Meta:
        verbose_name_plural = "comments"
        indexes = [
            models.Index(fields=['author', 'created_on', 'body']),
        ]