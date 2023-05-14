from django.contrib import admin
from django.urls import path
from listings import views

'''/<str:hash>'''
urlpatterns = [
    path("new-ads-listings/<str:uid>/",
         views.new_ad_listing, name='new_ad_listing'),
    path("ads/<str:id>/", views.single_page_ads, name='single_ads'),
    path("delete_listing/<str:uid>/<str:aid>/",
         views.delete_listing, name='delete_listing'),
    path("listing", views.all_listing, name="all_listing")
    # path("profile/<str:uid>/", views.profile, name='profile'),
]
