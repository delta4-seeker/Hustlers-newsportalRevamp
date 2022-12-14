import admin_thumbnails
from django.contrib import admin

# Register your models here.

from article import models
from article.models import ArticleCategory, Article, Images,  Review , ReaderInterest



class ArticleCategoryAdmin2(admin.ModelAdmin):
    list_display = ('title', 'status',
                    'image_tag', 'slug')
    list_display_links = ('status',)
    prepopulated_fields = {'slug': ('title',) ,'keywords': ('title',) ,'description': ('title',) , }

@admin_thumbnails.thumbnail('image')

class articleImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','image_thumbnail']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'status','image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [articleImageInline]
    prepopulated_fields = {'slug': ('title',) ,'keywords': ('title',) ,'description': ('title',) , }


class ReaderInterestAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',) ,'keywords': ('title',) ,'description': ('title',) , }


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['subject','review', 'status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','review','ip','user','article','rate','id')


admin.site.register(ArticleCategory,ArticleCategoryAdmin2)
admin.site.register(Article,ArticleAdmin)
admin.site.register(ReaderInterest,ReaderInterestAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Images,ImagesAdmin)
