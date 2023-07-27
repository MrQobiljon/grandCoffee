from django.contrib import admin

from .models import About, GalleryText, Gallery, Service, Comment, Message


admin.site.register(About)


class AdminGallery(admin.StackedInline):
    model = Gallery
    extra = 1


@admin.register(GalleryText)
class AdminGalleryText(admin.ModelAdmin):
    inlines = [AdminGallery]


admin.site.register(Service)
admin.site.register(Comment)
admin.site.register(Message)