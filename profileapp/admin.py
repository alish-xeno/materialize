from django.contrib import admin
from .models import *


admin.site.register(
    [Admin, GalleryImages, CustomerMessage, Specification, MessageSpecificationComment])

class ImageInline(admin.TabularInline):
    model = GalleryImages


class GallerySpecificationInline(admin.StackedInline):
    model = CustomerMessage


class GalleryAdmin(admin.ModelAdmin):
    inlines = (ImageInline, GallerySpecificationInline,
               # HouseSpecificInline, LandSpecificInline, FlatSpecificInline
               )


admin.site.register(Gallery, GalleryAdmin)