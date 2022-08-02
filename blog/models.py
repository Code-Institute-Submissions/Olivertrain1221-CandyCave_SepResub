from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Posts(models.Model):
    """
    Users Posts
    """
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,null=False, blank=False, on_delete=models.SET_DEFAULT, default=1)
    body = models.TextField(max_length=10000)
    slug = models.SlugField(max_length=128, unique=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:
            if slugify(self.title) != self.slug:
                self.slug = slugify(self.title)
        else:
            self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)