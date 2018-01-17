from django.http import HttpResponse
from django.shortcuts import render
from geopy.geocoders import Nominatim	
from location.models import Question
import datetime


def get_location(request):
	context = {}
	now = datetime.datetime.now()
	if request.method == "POST":
		geolocator = Nominatim()
		latitude = request.POST['latitude']
		longitude = request.POST['longitude']
		if Question.objects.filter(latitude=latitude,longitude=longitude,\
			).exists():
			location = Question.objects.filter(latitude=latitude,longitude=longitude)\
						.first()
			if location.date_added.date() != now.date():
				query = latitude+','+longitude
				location = geolocator.reverse(query)
				p = Question(latitude=latitude,longitude=latitude,address=location.address,\
					date_added=now)
				p.save()
		else:
			query = latitude+','+longitude
			location = geolocator.reverse(query)
			p = Question(latitude=latitude,longitude=latitude,address=location.address,\
				date_added=now)
			p.save()
		context = {
		"address": location.address
		}
		return render(request, 'location/location.html', context)

		pass
	else:
		return render(request, 'location/get_location.html', context)