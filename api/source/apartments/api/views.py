import json

from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Apartment


class ApartmentView(APIView):

	def get(self, request, id=None):
		# defualt response to return if /id path param provided, with invalid id
		response = Response(status=status.HTTP_404_NOT_FOUND)

		# return all apartments in /id is not provided as path param in url
		if not id:
			response = Response(Apartment.objects.all().values())

		# return a single apartment if /id is provided in url and apartment exists
		else:
			apartment = Apartment.objects.filter(pk=id).first()
			response = Response(model_to_dict(apartment)) if apartment else response
		return response


	def post(self, request):
		# fields to check POST request body against when adding apartments
		required_fields = [
			'number',
			'floor',
			'building',
			'city',
			'area_m2',
			'price',
			'description',
		]

		try:
			# read data directly from request body in stream and load as json
			data = request.stream.read().decode('utf-8')
			apartment = json.loads(data)

			# check if data is a dictionary and fields in 'required_fields' exist
			if not(type(apartment) == dict and list(apartment.keys()) == required_fields):
				raise ApartmentFormatExcpetion

		# exceptions to be thrown if any of the above scenarios does not go as intended
		except (json.decoder.JSONDecodeError, UnicodeEncodeError, ApartmentFormatExcpetion) as e:
			return Response('Please check apartment object format', status=status.HTTP_400_BAD_REQUEST)

		# if apartment already exists, return error response
		if Apartment.objects.filter(number=apartment['number'], floor=apartment['floor'], building=apartment['building'], city=apartment['city']):
			return Response(status=status.HTTP_409_CONFLICT)
		
		# if apartment created, return success response
		Apartment.objects.create(**apartment)
		return Response(status=status.HTTP_201_CREATED)
