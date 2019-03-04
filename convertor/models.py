import uuid

from django.db import models
from django.conf import settings


def post_filename(instance, filename):
    name = str(uuid.uuid4())
    ext = filename.split('.')[-1]
    new_filename = 'post/md/{0}.{1}'.format(name, ext)
    print(new_filename)
    return new_filename


class Post(models.Model):
    title = models.CharField(max_length=100)

    published_date = models.DateTimeField(auto_now_add=True)

    summary = models.TextField(
        blank=True,
        max_length=200
    )

    slug = models.SlugField(
        blank=False,
        db_index=True
    )

    page_md = models.FileField(blank=False, upload_to=post_filename)
    page_web = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-published_date']
