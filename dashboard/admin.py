from django.contrib import admin
from .models import Farmer, Farm, Crop, Activity, Harvest
@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = (
        "farmer_id",
        "name",
        "mobile",
        "village",
        "taluka",
        "district",
        "land_area_acres",
        "created_at",
    )

    search_fields = (
        "name",
        "mobile",
        "village",
        "district",
    )


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = (
        "farm_id",
        "farm_name",
        "farmer",
        "land_area_acres",
        "soil_type",
        "irrigation_type",
        "village",
        "created_at",
    )

    search_fields = (
        "farm_name",
        "village",
        "soil_type",
        "irrigation_type",
    )


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = (
        "crop_id",
        "crop_name",
        "farm",
        "season",
        "sowing_date",
        "expected_harvest_date",
        "area_acres",
        "created_at",
    )

    search_fields = (
        "crop_name",
        "season",
    )

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "activity_id",
        "activity_type",
        "crop",
        "activity_date",
        "cost",
        "created_at",
    )

    search_fields = (
        "activity_type",
        "description",
        "crop__crop_name",
    )

@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):
    list_display = (
        "harvest_id",
        "crop",
        "harvest_date",
        "quantity",
        "unit",
        "quality",
        "created_at",
    )

    search_fields = (
        "crop__crop_name",
        "quality",
        "unit",
    )