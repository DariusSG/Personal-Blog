import readtime

from django.contrib.auth.models import User
from django.db import models

from django.utils.functional import cached_property
from django.utils.text import slugify



class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    async def asave(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return await super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True,
                                  null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    prev_post = models.ForeignKey(
        'self', related_name='previous_post', on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name='Previous Post')
    nxt_post = models.ForeignKey(
        'self', related_name='next_post', on_delete=models.SET_NULL, null=True,
        blank=True, verbose_name='Next Post')

    def __str__(self):
        return self.title

    @cached_property
    def read_time(self):
        return readtime.of_markdown(self.content).minutes

    async def post_author(self):
        post_model = await Post.objects.select_related('author').aget(slug__exact=self.slug)
        return post_model.author

    async def asave(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return await super().asave(*args, **kwargs)

    async def arefresh_from_db(self, *args, **kwargs):
        await super(Post, self).arefresh_from_db(*args, **kwargs)
        cached_properties = [
            'read_time',
        ]
        for _property in cached_properties:
            try:
                del self.__dict__[_property]
            except KeyError:
                pass