from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import *
from .models import *
from accounts.models import User
from django.db.models import Count

# addProduct
# updateProduct
# disableProduct


@login_required(login_url='/sign_in/')
def new_ad_listing(request, uid):

    userDetails = User.objects.get(uid=uid)
    if request.method == 'GET':
        # cat_models_details = Category()
        details = Category.objects.all()
        # User.get_session_auth_hash
        return render(request, 'ad-listing.html', {'cat': details, 'userData': userDetails})

    if request.method == 'POST':
        title = request.POST.get('ads_title')
        gender = request.POST.get('gender')  # currently not in use
        cat_id = request.POST.get('adscategory')
        item_price = request.POST.get('price')
        description = request.POST.get('ads-description')
        nego = request.POST.get('is_negotiable')
        address = request.POST.get('location')
        if(nego != True):
            nego = False

        cat_id = Category.objects.get(cat_uid=cat_id)
        # for image in images:
        try:
            listing = ads.objects.create(
                ads_title=title,
                ads_description=description,
                price=item_price,
                category_id=cat_id,
                negotiable=nego,
                owner=userDetails,
                location=address
            )
            # if listing is not None:
            images = request.FILES.getlist('imagesFile')
            print(images)
            for imgs in images:
                product_image = Ads_Images.objects.create(
                    ads_id=listing,
                    ads_photos=imgs
                )
                print(product_image, " ", imgs)
                # if product_image is not None:
                # product_image.save()
        except Exception as e:
            print('Error : ', e)
        return redirect(f'/dashboard/{uid}/')


@login_required(login_url='/sign_in/')
def single_page_ads(request, id):
    if request.method == 'GET':
        # userDetails = ads.objects.get(owner=uid)
        adsDetails = ads.objects.get(ads_id=id)
        userImage = User.objects.get(email=adsDetails.owner)
        print(userImage)
        adsImages = Ads_Images.objects.all().filter(ads_id=adsDetails)
        # print(adsImages)
    return render(request, 'single-page-ads.html', {'details': adsDetails, 'image': adsImages, 'userImage': userImage})


@login_required(login_url='/sign_in/')
def delete_listing(request, uid, aid):
    # if request.method == 'POST':
    listing = ads.objects.get(owner=uid, ads_id=aid)
    print(f'{listing} {listing.ads_id}')

    temp = listing.delete()
    print(temp)
    # return HttpResponse(f'{temp} {listing} {aid}')
    return redirect(f'/dashboard/{uid}/')


def all_listing(request):
    if request.method == "GET":
        listing = ads.objects.all()
        categories = Category.objects.all()
        books_by_category = ads.objects.values('category_id').annotate(num_books=Count('category_id'))
        # context = {'books_by_category': books_by_category}
        print(books_by_category)
        # listing_Image = Ads_Images.objects.all()
        return render(request, 'listing.html', {"ads": listing, "cat":categories, "num" : books_by_category})
    # if request.method == "POST":

@login_required(login_url='/sign_in/')
def search_listing(request):
    if request.method == 'POST':
        q = request.POST.get('queryName')
        return render(request, 'listing.html', {})
