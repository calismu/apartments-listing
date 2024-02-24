from django.db import models


# Database ORM class for apartments, with typed fields for db columns

class Apartment(models.Model):
	number = models.PositiveIntegerField()
	floor = models.PositiveIntegerField()
	building = models.PositiveIntegerField()
	city = models.CharField(max_length=32)
	area_m2 = models.PositiveIntegerField()
	price = models.DecimalField(max_digits=11, decimal_places=2)
	description = models.TextField(null=True, default=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)