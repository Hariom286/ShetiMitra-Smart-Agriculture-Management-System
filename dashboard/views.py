import requests

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

from .models import Farmer, Farm, Crop, Activity, Harvest


# =========================
# HOME / DASHBOARD
# =========================

@login_required
def home(request):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 18.5204,
        "longitude": 73.8567,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
    }

    response = requests.get(url, params=params)
    weather_data = response.json()
    weather = weather_data["current"]

    weather_code = weather.get("weather_code")

    if weather_code == 0:
        weather["weather_status"] = "Clear Sky ☀️"
    elif weather_code in [1, 2, 3]:
        weather["weather_status"] = "Partly Cloudy ☁️"
    elif weather_code in [45, 48]:
        weather["weather_status"] = "Foggy 🌫️"
    elif weather_code in [51, 53, 55, 56, 57]:
        weather["weather_status"] = "Drizzle 🌦️"
    elif weather_code in [61, 63, 65, 66, 67]:
        weather["weather_status"] = "Rainy 🌧️"
    elif weather_code in [71, 73, 75, 77]:
        weather["weather_status"] = "Snowy ❄️"
    elif weather_code in [80, 81, 82]:
        weather["weather_status"] = "Rain Showers 🌦️"
    elif weather_code in [95, 96, 99]:
        weather["weather_status"] = "Thunderstorm ⛈️"
    else:
        weather["weather_status"] = "Unknown"

    return render(
        request,
        "dashboard/home.html",
        {"weather": weather}
    )


# =========================
# FARMER MANAGEMENT
# =========================

@login_required
def farmer_list(request):
    farmers = Farmer.objects.filter(user=request.user)

    return render(
        request,
        "dashboard/farmer_list.html",
        {"farmers": farmers}
    )


@login_required
def farmer_add(request):
    if request.method == "POST":

        Farmer.objects.create(
            user=request.user,
            name=request.POST.get("name"),
            mobile=request.POST.get("mobile"),
            village=request.POST.get("village"),
            taluka=request.POST.get("taluka"),
            district=request.POST.get("district"),
            land_area_acres=request.POST.get("land_area_acres"),
        )

        return redirect("farmer_list")

    return render(
        request,
        "dashboard/farmer_add.html"
    )


@login_required
def farmer_edit(request, farmer_id):

    farmer = get_object_or_404(
        Farmer,
        farmer_id=farmer_id,
        user=request.user
    )

    if request.method == "POST":

        farmer.name = request.POST.get("name")
        farmer.mobile = request.POST.get("mobile")
        farmer.village = request.POST.get("village")
        farmer.taluka = request.POST.get("taluka")
        farmer.district = request.POST.get("district")
        farmer.land_area_acres = request.POST.get("land_area_acres")

        farmer.save()

        return redirect("farmer_list")

    return render(
        request,
        "dashboard/farmer_edit.html",
        {"farmer": farmer}
    )


@login_required
def farmer_delete(request, farmer_id):

    farmer = get_object_or_404(
        Farmer,
        farmer_id=farmer_id,
        user=request.user
    )

    if request.method == "POST":

        farmer.delete()

        return redirect("farmer_list")

    return render(
        request,
        "dashboard/farmer_delete.html",
        {"farmer": farmer}
    )


# =========================
# FARM MANAGEMENT
# =========================

@login_required
def farm_list(request):

    farms = Farm.objects.filter(
        farmer__user=request.user
    )

    return render(
        request,
        "dashboard/farm_list.html",
        {"farms": farms}
    )


@login_required
def farm_add(request):

    farmers = Farmer.objects.filter(
        user=request.user
    )

    if request.method == "POST":

        farmer_id = request.POST.get("farmer")

        farmer = get_object_or_404(
            Farmer,
            farmer_id=farmer_id,
            user=request.user
        )

        Farm.objects.create(
            farmer=farmer,
            farm_name=request.POST.get("farm_name"),
            land_area_acres=request.POST.get("land_area_acres"),
            soil_type=request.POST.get("soil_type"),
            irrigation_type=request.POST.get("irrigation_type"),
            village=request.POST.get("village"),
        )

        return redirect("farm_list")

    return render(
        request,
        "dashboard/farm_add.html",
        {"farmers": farmers}
    )


@login_required
def farm_edit(request, farm_id):

    farm = get_object_or_404(
        Farm,
        farm_id=farm_id,
        farmer__user=request.user
    )

    farmers = Farmer.objects.filter(
        user=request.user
    )

    if request.method == "POST":

        farmer_id = request.POST.get("farmer")

        farmer = get_object_or_404(
            Farmer,
            farmer_id=farmer_id,
            user=request.user
        )

        farm.farmer = farmer
        farm.farm_name = request.POST.get("farm_name")
        farm.land_area_acres = request.POST.get("land_area_acres")
        farm.soil_type = request.POST.get("soil_type")
        farm.irrigation_type = request.POST.get("irrigation_type")
        farm.village = request.POST.get("village")

        farm.save()

        return redirect("farm_list")

    return render(
        request,
        "dashboard/farm_edit.html",
        {
            "farm": farm,
            "farmers": farmers
        }
    )


@login_required
def farm_delete(request, farm_id):

    farm = get_object_or_404(
        Farm,
        farm_id=farm_id,
        farmer__user=request.user
    )

    if request.method == "POST":

        farm.delete()

        return redirect("farm_list")

    return render(
        request,
        "dashboard/farm_delete.html",
        {"farm": farm}
    )


# =========================
# CROP MANAGEMENT
# =========================

@login_required
def crop_list(request):

    crops = Crop.objects.filter(
        farm__farmer__user=request.user
    )

    return render(
        request,
        "dashboard/crop_list.html",
        {"crops": crops}
    )


@login_required
def crop_add(request):

    farms = Farm.objects.filter(
        farmer__user=request.user
    )

    if request.method == "POST":

        farm_id = request.POST.get("farm")

        farm = get_object_or_404(
            Farm,
            farm_id=farm_id,
            farmer__user=request.user
        )

        Crop.objects.create(
            farm=farm,
            crop_name=request.POST.get("crop_name"),
            season=request.POST.get("season"),
            sowing_date=request.POST.get("sowing_date"),
            expected_harvest_date=request.POST.get(
                "expected_harvest_date"
            ),
            area_acres=request.POST.get("area_acres"),
        )

        return redirect("crop_list")

    return render(
        request,
        "dashboard/crop_add.html",
        {"farms": farms}
    )


@login_required
def crop_edit(request, crop_id):

    crop = get_object_or_404(
        Crop,
        crop_id=crop_id,
        farm__farmer__user=request.user
    )

    farms = Farm.objects.filter(
        farmer__user=request.user
    )

    if request.method == "POST":

        farm_id = request.POST.get("farm")

        farm = get_object_or_404(
            Farm,
            farm_id=farm_id,
            farmer__user=request.user
        )

        crop.farm = farm
        crop.crop_name = request.POST.get("crop_name")
        crop.season = request.POST.get("season")
        crop.sowing_date = request.POST.get("sowing_date")
        crop.expected_harvest_date = request.POST.get(
            "expected_harvest_date"
        )
        crop.area_acres = request.POST.get("area_acres")

        crop.save()

        return redirect("crop_list")

    return render(
        request,
        "dashboard/crop_edit.html",
        {
            "crop": crop,
            "farms": farms
        }
    )


@login_required
def crop_delete(request, crop_id):

    crop = get_object_or_404(
        Crop,
        crop_id=crop_id,
        farm__farmer__user=request.user
    )

    if request.method == "POST":

        crop.delete()

        return redirect("crop_list")

    return render(
        request,
        "dashboard/crop_delete.html",
        {"crop": crop}
    )


# =========================
# FARMING ACTIVITIES
# =========================

@login_required
def activity_list(request):

    activities = Activity.objects.filter(
        crop__farm__farmer__user=request.user
    )

    return render(
        request,
        "dashboard/activity_list.html",
        {"activities": activities}
    )


@login_required
def activity_add(request):

    crops = Crop.objects.filter(
        farm__farmer__user=request.user
    )

    if request.method == "POST":

        crop_id = request.POST.get("crop")

        crop = get_object_or_404(
            Crop,
            crop_id=crop_id,
            farm__farmer__user=request.user
        )

        Activity.objects.create(
            crop=crop,
            activity_type=request.POST.get("activity_type"),
            activity_date=request.POST.get("activity_date"),
            description=request.POST.get("description"),
            cost=request.POST.get("cost"),
        )

        return redirect("activity_list")

    return render(
        request,
        "dashboard/activity_add.html",
        {"crops": crops}
    )


@login_required
def activity_edit(request, activity_id):

    activity = get_object_or_404(
        Activity,
        activity_id=activity_id,
        crop__farm__farmer__user=request.user
    )

    crops = Crop.objects.filter(
        farm__farmer__user=request.user
    )

    if request.method == "POST":

        crop_id = request.POST.get("crop")

        crop = get_object_or_404(
            Crop,
            crop_id=crop_id,
            farm__farmer__user=request.user
        )

        activity.crop = crop
        activity.activity_type = request.POST.get("activity_type")
        activity.activity_date = request.POST.get("activity_date")
        activity.description = request.POST.get("description")
        activity.cost = request.POST.get("cost")

        activity.save()

        return redirect("activity_list")

    return render(
        request,
        "dashboard/activity_edit.html",
        {
            "activity": activity,
            "crops": crops
        }
    )


@login_required
def activity_delete(request, activity_id):

    activity = get_object_or_404(
        Activity,
        activity_id=activity_id,
        crop__farm__farmer__user=request.user
    )

    if request.method == "POST":

        activity.delete()

        return redirect("activity_list")

    return render(
        request,
        "dashboard/activity_delete.html",
        {"activity": activity}
    )


# =========================
# HARVEST MANAGEMENT
# =========================

@login_required
def harvest_list(request):

    harvests = Harvest.objects.filter(
        crop__farm__farmer__user=request.user
    )

    return render(
        request,
        "dashboard/harvest_list.html",
        {"harvests": harvests}
    )


@login_required
def harvest_add(request):

    crops = Crop.objects.filter(
        farm__farmer__user=request.user
    )

    if request.method == "POST":

        crop_id = request.POST.get("crop")

        crop = get_object_or_404(
            Crop,
            crop_id=crop_id,
            farm__farmer__user=request.user
        )

        Harvest.objects.create(
            crop=crop,
            harvest_date=request.POST.get("harvest_date"),
            quantity=request.POST.get("quantity"),
            unit=request.POST.get("unit"),
            quality=request.POST.get("quality"),
            notes=request.POST.get("notes"),
        )

        return redirect("harvest_list")

    return render(
        request,
        "dashboard/harvest_add.html",
        {"crops": crops}
    )


@login_required
def harvest_edit(request, harvest_id):

    harvest = get_object_or_404(
        Harvest,
        harvest_id=harvest_id,
        crop__farm__farmer__user=request.user
    )

    crops = Crop.objects.filter(
        farm__farmer__user=request.user
    )

    if request.method == "POST":

        crop_id = request.POST.get("crop")

        crop = get_object_or_404(
            Crop,
            crop_id=crop_id,
            farm__farmer__user=request.user
        )

        harvest.crop = crop
        harvest.harvest_date = request.POST.get("harvest_date")
        harvest.quantity = request.POST.get("quantity")
        harvest.unit = request.POST.get("unit")
        harvest.quality = request.POST.get("quality")
        harvest.notes = request.POST.get("notes")

        harvest.save()

        return redirect("harvest_list")

    return render(
        request,
        "dashboard/harvest_edit.html",
        {
            "harvest": harvest,
            "crops": crops
        }
    )


@login_required
def harvest_delete(request, harvest_id):

    harvest = get_object_or_404(
        Harvest,
        harvest_id=harvest_id,
        crop__farm__farmer__user=request.user
    )

    if request.method == "POST":

        harvest.delete()

        return redirect("harvest_list")

    return render(
        request,
        "dashboard/harvest_delete.html",
        {"harvest": harvest}
    )


# =========================
# REPORTS
# =========================

@login_required
def reports(request):

    farmers = Farmer.objects.filter(
        user=request.user
    )

    farms = Farm.objects.filter(
        farmer__user=request.user
    )

    crops = Crop.objects.filter(
        farm__farmer__user=request.user
    )

    activities = Activity.objects.filter(
        crop__farm__farmer__user=request.user
    ).select_related("crop")

    harvests = Harvest.objects.filter(
        crop__farm__farmer__user=request.user
    ).select_related("crop")

    total_activity_cost = (
        activities.aggregate(total=Sum("cost"))["total"] or 0
    )

    crop_costs = (
        activities
        .values("crop__crop_name")
        .annotate(total_cost=Sum("cost"))
        .order_by("crop__crop_name")
    )

    return render(
        request,
        "dashboard/reports.html",
        {
            "farmers": farmers,
            "farms": farms,
            "crops": crops,
            "activities": activities,
            "harvests": harvests,
            "total_activity_cost": total_activity_cost,
            "crop_costs": crop_costs,
        }
    )