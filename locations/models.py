from django.db import models

# Nomenclature of classes based on https://goo.gl/2B5Q4U


class Venue(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    # FIXME from django.contrib.gis.db.models import PointField
    # (but we need postgresql)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    photo = models.ImageField(
        upload_to='events/locations/venue/',
        blank=True
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    venue = models.ForeignKey(
        Venue,
        on_delete=models.PROTECT,
        related_name='locations'
    )
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='events/locations/location/',
        blank=True
    )

    def __str__(self):
        return self.name
