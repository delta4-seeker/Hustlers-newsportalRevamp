from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe

class ArticleCategory(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=False,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS , default='True')
    slug = models.SlugField(null=False, unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

class ReaderInterest(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=False,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS , default='True')
    slug = models.SlugField(null=False, unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

class Article(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE) #many to one relation with Category
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(upload_to='images/',null=False)
    audio=models.FileField(upload_to='images/',null=False)
    content=RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    status=models.CharField(max_length=10,choices=STATUS, default='True')
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
        reviews = Review.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Review.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt


class Images(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=False, upload_to='images/')

    def __str__(self):
        return self.title

class Review(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
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

class CommentForm(ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'review', 'rate']
