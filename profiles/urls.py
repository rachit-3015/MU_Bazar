from django.urls import path
from profiles import views


urlpatterns = [
    path("profile/<str:uid>/", views.profile, name='profile'),
    path("dashboard/<str:uid>/", views.dashboard, name='dashboard'),
    path("wishlist/<str:uid>/", views.wishlist, name='wishlist'),
    path("profilePersonalUpdate/<str:uid>/",
         views.profilePersonalUpdate, name='profilePersonalUpdate'),
]
