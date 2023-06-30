from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render

from MobileSellingApp.forms import ProfileForm, MobileListingForm
from MobileSellingApp.models import Profile, MobileListing


# Create your views here.


def index(request):
    qs = MobileListing.objects.all()[:4]
    context = {'listings': qs}
    return render(request, 'pages/index.html', context=context)


def login(request):
    context = {'errors': ''}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_auth(request, user)
            return HttpResponseRedirect('/index')
        else:
            context = {'errors': 'Invalid Username Or Password'}
            return render(request, 'pages/login.html', context=context)
    return render(request, 'pages/login.html', context=context)


@login_required
def logout(request):
    logout_auth(request)
    return HttpResponseRedirect('/index')


def register(request):
    if request.method == 'POST':
        form_data = ProfileForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            prof = form_data.save(commit=False)
            if User.objects.filter(first_name=prof.profile_email).count() <= 0:
                u = User.objects.create_user(prof.profile_email, password=prof.profile_password, is_staff=True)
                group = Group.objects.get(name="StandardUserGroup")
                group.user_set.add(u)
                prof.profile_user = u
                prof.profile_image = form_data.cleaned_data['profile_image']
                prof.save()
                return HttpResponseRedirect('/login')
        return HttpResponseRedirect('/index')

    context = {'form': ProfileForm}
    return render(request, 'pages/register.html', context=context)


def contact(request):
    return render(request, 'pages/contact.html')


@login_required
def addlisting(request):
    if request.method == 'POST':
        form_data = MobileListingForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            listing = form_data.save(commit=False)
            listing.listing_profile = Profile.objects.filter(profile_user=request.user.id).get()
            listing.listing_image = form_data.cleaned_data['listing_image']
            listing.save()
            return HttpResponseRedirect('/index')
        return HttpResponseRedirect('/addlisting')

    context = {'form': MobileListingForm}
    return render(request, 'pages/addlisting.html', context=context)


def listings(request):
    if request.method == 'POST':
        search = request.POST['search']
        print(search)
        qs = MobileListing.objects.filter(listing_title__contains=search)
        context = {'listings': qs}
        return render(request, 'pages/listings.html', context=context)

    qs = MobileListing.objects.all()
    context = {'listings': qs}
    return render(request, 'pages/listings.html', context=context)
