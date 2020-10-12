from django.db import models
from django.contrib.auth.models import User, Group
from .utils import unique_slug_generator


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True



class Admin(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="admin", null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    contact_no = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    google = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        group, group_created = Group.objects.get_or_create(name="SuperAdmin")
        self.user.groups.add(group)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Gallery(TimeStamp):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    caption = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class GalleryImages(TimeStamp):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="gallery")
    caption = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.gallery.title
