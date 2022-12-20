import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation

from home.forms import SearchForm
from home.models import Setting, ContactForm, ContactMessage, FAQ, SettingLang, Language
from mysite import settings
from article.models import Article, ArticleCategory, Images , ReaderInterest
from user.models import UserProfile


def index(request):
    current_user = request.user
    setting = Setting.objects.get(pk=1)
    category = ArticleCategory.objects.all() # last 4 products
    article = Article.objects.all() # last 4 products
    featured = Article.objects.all().order_by('?')[:2] # last 4 products
    interest = ReaderInterest.objects.all() # last 4 products

    page="home"
    context={'setting':setting,
             'current_user':current_user,
             'page':page,
             'category':category,
             'interest':interest,
             'featured':featured,
             'article':article
             }
    return render(request,'index.html',context)



