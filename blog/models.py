from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars


class Category(models.Model):
    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "categories"


class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # da sistemare, non voglio eliminare un utente scrittore e di consegurenza anche tutti i suoi post. Voglio poter eliminare solo l' utente e mantenere i post magari settando l'author su None
    image = models.ImageField(upload_to="images/")
    slug = models.SlugField(unique=True, max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    categories = models.ManyToManyField('Category', related_name = 'posts')
   
    def __str__(self):
        return self.title

    # short description in admin page
    @property
    def short_description(self):
        return truncatechars(self.body, 100)
    
    class Meta:
        verbose_name_plural = "posts"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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
