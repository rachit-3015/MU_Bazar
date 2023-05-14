from django.shortcuts import render, redirect
from django.contrib.auth.decorators import *
from accounts.models import User
from listings.models import ads, Ads_Images, Category
from django.contrib import messages


# Create your views here.


@login_required(login_url='/sign_in/')
def profile(request, uid):
    # ent = User.email.get()
    if request.method == "GET":
        # row = request.objects.get('username': email)
        userDetails = User.objects.get(uid=uid)
        print(userDetails.user_image)
        return render(request, 'userProfile.html', {"data": userDetails})

    # if request.status_code == 200:


@login_required(login_url='/sign_in/')
def dashboard(request, uid):
    if request.method == "GET":
        userDetails = User.objects.get(uid=uid)
        category = Category.objects.all()
        listingDetails = ads.objects.all().filter(owner=uid).order_by('-time')
        # print(userDetails.user_image)
        print(category)

    return render(request, 'dashboard.html', {"data": userDetails, "listing": listingDetails, "cat" : category})


@login_required(login_url='/sign_in/')
def wishlist(request, uid):
    userDetails = User.objects.get(uid=uid)
    return render(request, 'user-wishlist.html',{ "data": userDetails})


@login_required(login_url='/sign_in/')
def profilePersonalUpdate(request, uid):
    if request.method == "POST":
        setUser = User.objects.get(uid=uid)
        print("Image here: "+str(setUser.user_image))
        try:
            firstName = request.POST.get('firstName')
            lastName = request.POST.get('lastName')
            profileImage = request.FILES.getlist('profilePicture')
            # print("Printing Statement : " + str(profileImage))
        except Exception as e:
            print("Exception Image : " + str(setUser.user_image))
            profileImage = setUser.user_image
            # messages.error(request, f'{e}')
            # return redirect(f'/profile/{uid}')
        print("Updated Image here: "+str(profileImage))

        setUser.first_name = firstName
        setUser.last_name = lastName

        # print(str(setUser.user_image))
        if setUser.user_image == profileImage:
            pass
        else:
            setUser.user_image.delete()
            # setUser.user_image.delete()
            setUser.user_image = profileImage
            # pass
        # setUser.save()
        # print(profileImage)
        # product.save(update_fields=['name'])
        if str(setUser.save()):
            messages.success(request, "Record Updated")
        else:
            messages.error(request, "Record Not Updated")

    return redirect(f'/profile/{uid}')
