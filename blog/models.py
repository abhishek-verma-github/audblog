from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import settings
# from model_utils import Choices
# from django import forms
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
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


# class BlogTag(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
