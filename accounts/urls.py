from django.urls import path

from .views import (
    ShetiMitraLoginView,
    ShetiMitraLogoutView,
    register,
)


urlpatterns = [

    path(
        '',
        ShetiMitraLoginView.as_view(),
        name='login'
    ),

    path(
        'register/',
        register,
        name='register'
    ),

    path(
        'logout/',
        ShetiMitraLogoutView.as_view(),
        name='logout'
    ),

]