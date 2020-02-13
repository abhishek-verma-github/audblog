from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import settings
# from model_utils import Choices
# from django import forms
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from PIL import Image, ImageChops

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['title'], name='unique_category')]

    def __str__(self):
        return self.title


class ChildCategory(models.Model):
    title = models.CharField(max_length=120)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['title'], name='unique_child_category')]

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['title'], name='unique_tag')]

    def __str__(self):
        return self.title


class Blog(models.Model):
    blogImage = models.ImageField(null=True,
                                  upload_to='blog_pictures')
    title = models.CharField(max_length=120)
    content = RichTextUploadingField(blank=True, null=True)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(ChildCategory, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['title'], name='unique_blog')]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.blogImage.path)

        if img.height > 1024 and img.width > 1024:
            output_size = (1024, 640)
            #
            # left = 155
            # top = 65
            # right = 360
            # bottom = 270
            width, height = img.size

            if height > width:
                delta = height - width
                left = int(delta / 4)
                upper = 0
                right = height + left
                lower = height
            else:
                delta = width - height
                left = 0
                upper = int(delta / 4)
                right = width
                lower = width + upper

            img.thumbnail(output_size)
            img1 = img.crop((left, upper, right, lower))
            img.save(self.image.path)

    # def image_tag(self):
    #     from django.utils.html import format_html
    #     return format_html('<img src="{}" />'.format(self.blogImage.url))
    # image_tag.short_description = 'blogImage'
    # image_tag.allow_tags = True


# class BlogTag(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
