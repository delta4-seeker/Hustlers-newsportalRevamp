from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from home.models import Language


class PartnerSchool(models.Model):
    name = models.CharField(max_length=50,blank=True)
    address = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=50,blank=True)
    logo = models.ImageField(blank=True, upload_to='images/')
    banner = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.name
    
    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

class Magazine(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

 
    school = models.ForeignKey(PartnerSchool, on_delete=models.CASCADE) #many to one relation with Category
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    coverimage=models.ImageField(upload_to='images/',null=False)
    editor = models.CharField(max_length=255 , default= "student")
    detail=RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    status=models.CharField(max_length=10,choices=STATUS , default="True")
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def image_tag(self):
        if self.coverimage.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.coverimage.url))
        else:
            return ""




class SchoolArtImages(models.Model):
    magazine=models.ForeignKey(Magazine,on_delete=models.CASCADE)
    artist = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.artist



class SchoolArticle(models.Model):


    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE) #many to one relation with Category
    title = models.CharField(max_length=150)
    image=models.ImageField(upload_to='images/',null=False)
    writer =  models.CharField(max_length=150)
    content=RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    status=models.CharField(max_length=10,choices=STATUS , default="True")
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def avaregereview(self):
        reviews = SchoolReview.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = SchoolReview.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt


class SchoolReview(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    article=models.ForeignKey(SchoolArticle,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    review = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class SchoolCommentForm(ModelForm):
    class Meta:
        model = SchoolReview
        fields = ['subject', 'review', 'rate']

