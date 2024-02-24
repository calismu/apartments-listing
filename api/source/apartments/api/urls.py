from django.urls import path, include

from api.views import ApartmentView


urlpatterns = [
	# pattern to accept /app/apartments. returns all apartments
	path('apartments', ApartmentView.as_view(), name='apartment'),

	# pattern to accept /app/apartments/<apartment-id>. returns a single apartment if available
	path('apartments/<int:id>', ApartmentView.as_view(), name='apartment'),
]