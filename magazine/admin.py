import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from article import models
from magazine.models import SchoolArticle,PartnerSchool,SchoolArtImages,SchoolReview



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
    list_display = ['title','image', 'school']
    list_filter = ['school']


admin.site.register(SchoolArtImages,SchoolArtImagesAdmin)
admin.site.register(SchoolReview,SchoolReviewAdmin)
admin.site.register(PartnerSchool ,PartnerSchoolAdmin)
admin.site.register(SchoolArticle,SchoolArticleAdmin)
