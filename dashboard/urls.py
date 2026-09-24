from django.urls import path

from . import views


urlpatterns = [

    # HOME
    path(
        '',
        views.home,
        name='home'
    ),

    # =========================
    # FARMER MANAGEMENT
    # =========================

    path(
        'farmers/',
        views.farmer_list,
        name='farmer_list'
    ),

    path(
        'farmers/add/',
        views.farmer_add,
        name='farmer_add'
    ),

    path(
        'farmers/edit/<int:farmer_id>/',
        views.farmer_edit,
        name='farmer_edit'
    ),

    path(
        'farmers/delete/<int:farmer_id>/',
        views.farmer_delete,
        name='farmer_delete'
    ),

    # =========================
    # FARM MANAGEMENT
    # =========================

    path(
        'farms/',
        views.farm_list,
        name='farm_list'
    ),

    path(
        'farms/add/',
        views.farm_add,
        name='farm_add'
    ),

    path(
        'farms/edit/<int:farm_id>/',
        views.farm_edit,
        name='farm_edit'
    ),

    path(
        'farms/delete/<int:farm_id>/',
        views.farm_delete,
        name='farm_delete'
    ),

    # =========================
    # CROP MANAGEMENT
    # =========================

    path(
        'crops/',
        views.crop_list,
        name='crop_list'
    ),

    path(
        'crops/add/',
        views.crop_add,
        name='crop_add'
    ),

    path(
        'crops/edit/<int:crop_id>/',
        views.crop_edit,
        name='crop_edit'
    ),

    path(
        'crops/delete/<int:crop_id>/',
        views.crop_delete,
        name='crop_delete'
    ),

        # =========================
    # ACTIVITY MANAGEMENT
    # =========================

    path(
        'activities/',
        views.activity_list,
        name='activity_list'
    ),

    path(
        'activities/add/',
        views.activity_add,
        name='activity_add'
    ),

        path(
        'activities/edit/<int:activity_id>/',
        views.activity_edit,
        name='activity_edit'
    ),

    path(
        'activities/delete/<int:activity_id>/',
        views.activity_delete,
        name='activity_delete'
    ),

        # =========================
    # HARVEST MANAGEMENT
    # =========================

    path(
        'harvests/',
        views.harvest_list,
        name='harvest_list'
    ),

    path(
        'harvests/add/',
        views.harvest_add,
        name='harvest_add'
    ),

        path(
        'harvests/edit/<int:harvest_id>/',
        views.harvest_edit,
        name='harvest_edit'
    ),

    path(
        'harvests/delete/<int:harvest_id>/',
        views.harvest_delete,
        name='harvest_delete'
    ),

    path('reports/', views.reports, name='reports'),
]