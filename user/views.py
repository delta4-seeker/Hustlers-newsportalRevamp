from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from magazine.models import Magazine

# Create your views here.
from django.utils import translation

from home.models import FAQ
from article.models import ArticleCategory, Review
from magazine.models import SchoolArticle , SchoolArtImages , PartnerSchool
from user.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from user.models import UserProfile

@login_required(login_url='/login') # Check login
def index(request):
    #ArticleCategory = ArticleCategory.objects.all()
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {#'ArticleCategory': ArticleCategory,
               'profile':profile}
    return render(request,'user_profile.html',context)

@login_required(login_url='/login') # Check login
def magazine(request):
    category = ArticleCategory.objects.all()
    magazine1 = Magazine.objects.all()[:1]
        
    magazine2 = Magazine.objects.all()[1:2]
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'magazine1':magazine1,
               'magazine2':magazine2,
               'profile':profile
               
               }
    return render(request,'magazine.html' ,context)

def magazine_detail(request , id ): 
    category = ArticleCategory.objects.all()
    magazine = Magazine.objects.get(id = id )
    articles  = SchoolArticle.objects.filter(magazine = id)
    arts = SchoolArtImages.objects.filter(magazine = id)
    school = PartnerSchool.objects.get(id = magazine.school.id)
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'magazine':magazine,
               'articles':articles,
               'school':school,
               'arts':arts,
               'profile':profile
               }
    return render(request,'magazine_detail.html' ,context)


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user =request.user
            # userprofile=UserProfile.objects.get(user_id=current_user.id)
            # request.session['userimage'] = userprofile.image.url
            #*** Multi Langugae
            category = ArticleCategory.objects.all()
            context = {'category': category
            }
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/login')
    # Return an 'invalid login' error message.

    category = ArticleCategory.objects.all()
    context = {'category': category
     }
    return render(request, 'login_form.html',context)

def logout_func(request):
    logout(request)
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
        del request.session['currency']
    return HttpResponseRedirect('/')


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            # data=UserProfile()
            # data.user_id=current_user.id
            # data.image="images/users/user.png"
            # data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')


    form = SignUpForm()
    category = ArticleCategory.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request, 'signup_form.html', context)




@login_required(login_url='/login') # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        # profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        ArticleCategory = ArticleCategory.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'ArticleCategory': ArticleCategory,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)

@login_required(login_url='/login') # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        #ArticleCategory = ArticleCategory.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password.html', {'form': form,#'ArticleCategory': ArticleCategory
                       })

