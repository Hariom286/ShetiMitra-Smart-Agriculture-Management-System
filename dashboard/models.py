from django.db import models
from django.contrib.auth.models import User


class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="farmer_profile",
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    village = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    land_area_acres = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Farm(models.Model):
    farm_id = models.AutoField(primary_key=True)

    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name="farms"
    )

    farm_name = models.CharField(max_length=100)

    land_area_acres = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    soil_type = models.CharField(max_length=100)
    irrigation_type = models.CharField(max_length=100)
    village = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.farm_name


class Crop(models.Model):
    crop_id = models.AutoField(primary_key=True)

    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        related_name="crops"
    )

    crop_name = models.CharField(max_length=100)
    season = models.CharField(max_length=50)

    sowing_date = models.DateField()
    expected_harvest_date = models.DateField()

    area_acres = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crop_name


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)

    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name="activities"
    )

    activity_type = models.CharField(max_length=100)

    activity_date = models.DateField()

    description = models.TextField(blank=True)

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_type


class Harvest(models.Model):
    harvest_id = models.AutoField(primary_key=True)

    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name="harvests"
    )

    harvest_date = models.DateField()

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    unit = models.CharField(max_length=20)

    quality = models.CharField(
        max_length=100,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.crop.crop_name} - {self.harvest_date}"