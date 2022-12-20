import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from article import models
from magazine.models import SchoolArticle,PartnerSchool,SchoolArtImages,SchoolReview , Magazine



class SchoolArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','image_tag' , 'create_at']
    list_filter = ['status']
    readonly_fields = ('image_tag',)


class PartnerSchoolAdmin(admin.ModelAdmin):
    list_display = ['name','address', 'phone','image_tag']
    readonly_fields = ('image_tag',)


class SchoolReviewAdmin(admin.ModelAdmin):
    list_display = ['subject','review', 'status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','review','ip','user','article','rate','id')



class SchoolArtImagesAdmin(admin.ModelAdmin):
    list_display = [ 'artist' , 'image', 'magazine']
    list_filter = ['magazine']

@admin_thumbnails.thumbnail('image')
class SchoolArtInline(admin.TabularInline):
    model = SchoolArtImages
    readonly_fields = ('id',)
    readonly_fields = ('id',)
    fields = [ 'artist' ,  "image" ]
    show_change_link = True
    extra = 1
@admin_thumbnails.thumbnail('image')
class SchoolArticleInline(admin.TabularInline):
    model = SchoolArticle
    readonly_fields = ('id',)
    fields = [ "title" , "writer","image" , "content" ]
    show_change_link = True
    # prepopulated_fields = {'slug': ('title',)}
    extra = 1

class SchoolMagazineAdmin(admin.ModelAdmin):
    list_display = ['title','school', 'status','image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)
    inlines = [SchoolArticleInline,SchoolArtInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(SchoolArtImages,SchoolArtImagesAdmin)
admin.site.register(SchoolReview,SchoolReviewAdmin)
admin.site.register(PartnerSchool ,PartnerSchoolAdmin)
admin.site.register(SchoolArticle,SchoolArticleAdmin)
admin.site.register(Magazine,SchoolMagazineAdmin)
