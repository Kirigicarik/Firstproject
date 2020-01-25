from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Image = models.ImageField()
    Content = RichTextField()
    Tag = models.CharField(max_length=100)
    Slug = models.SlugField(max_length=20, unique=True)
    Date = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ('-Date',)


def __str__(self):
    return self.Title


def __unicode__(self):
    return u'%s' % self.Title


class comment(models.Model):
    Post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Body = models.TextField()
    Created = models.DateTimeField(auto_now_add=True)
    Active = models.BooleanField(default=True)
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ('Created',)

    def __str__(self):
        return 'comment By {}'.format(self.Name)
