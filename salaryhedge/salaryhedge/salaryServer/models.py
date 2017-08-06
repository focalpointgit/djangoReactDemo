from django.db import models


# Create your models here.
class Address(models.Model):
    street_number = models.CharField(max_length=20, blank=True)
    street_name = models.CharField(max_length=200)
    street_type = models.CharField(max_length=30)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=20)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

class Asset(models.Model):
    name = models.CharField(max_length=50)
    residance = models.ForeignKey(Address, on_delete=models.CASCADE)
# 3 buckets


# Size of Firm

# Candidate Background

# Market Conditions