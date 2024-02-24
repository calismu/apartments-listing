from decimal import Decimal

from api.models import Apartment


APARTMENTS = [
	{
		'number': 16,
		'floor': 5,
		'building': 3,
		'city': 'Cairo',
		'area_m2': 160,
		'price': Decimal(500000.00),
		'description': 'Large apartment with 2 balconies, 3 bedrooms and a great view overlooking a garden with no traffic around - 1653',
	},
	{
		'number': 12,
		'floor': 3,
		'building': 15,
		'city': 'Cairo',
		'area_m2': 200,
		'price': Decimal(5000000.55),
		'description': None,
	},
	{
		'number': 30,
		'floor': 5,
		'building': 1,
		'city': 'Cairo',
		'area_m2': 250,
		'price': Decimal(7000000),
		'description': 'Large apartment with 2 balconies, 3 bedrooms and a great view overlooking a garden with no traffic around - 3051',
	},
	{
		'number': 1,
		'floor': 0,
		'building': 50,
		'city': 'Cairo',
		'area_m2': 200,
		'price': Decimal(4500000),
		'description': 'Large apartment with 2 balconies, 3 bedrooms and a great view overlooking a garden with no traffic around - 1050',
	},
	{
		'number': 30,
		'floor': 15,
		'building': 3,
		'city': 'Alexandria',
		'area_m2': 200,
		'price': Decimal(8800000.05),
		'description': 'Large apartment with 2 balconies, 3 bedrooms and a great view overlooking a garden with no traffic around - 30153',
	},
	{
		'number': 12,
		'floor': 3,
		'building': 15,
		'city': 'Alexandria',
		'area_m2': 200,
		'price': Decimal(5000000.55),
		'description': 'Large apartment with 2 balconies, 3 bedrooms and a great view overlooking a garden with no traffic around - 12315',
	},
	{
		'number': 33,
		'floor': 5,
		'building': 90,
		'city': 'Alexandria',
		'area_m2': 100,
		'price': Decimal(1500000.55),
		'description': 'Large apartment with 2 balconies, 3 bedrooms and a great view overlooking a garden with no traffic around - 33590',
	},
]



# loop over apartments and create entries in the database
def fill_db(apartments):
	for apartment in apartments:
		Apartment.objects.create(
			number = apartment['number'],
			floor = apartment['floor'],
			building = apartment['building'],
			city = apartment['city'],
			area_m2 = apartment['area_m2'],
			price = apartment['price'],
			description = apartment['description']
		)


fill_db(APARTMENTS)