'''
Authors: Max Aguirre, Brandon Bower, Mapuana Maka

This file contains the following functios:

to_utm_list: Takes a list of points (tuples of lattitude and longitude)
and converts them to the UTM Coordinate System, with a small modification
to better apply it for the purposes of the Reverse Geocoding app.

calculate_utm_distances: Takes in a list of points in the "modified" UTM
system (as outputed by the above method), calculates the distance between
each pair of points, and outputs the distances, in meters, as a list.

calculate_latlong_distances: Takes a list of points (tuples of lattitude 
and longitude),  calculates the distance between each pair of points, and 
outputs the distances, in meters, as a list.

NOTE: calculate_utm_distances and calculate_latlong_distances have a very
similar functionality, but when testing, there is a difference of 1 cm every
15 meters. We have not done enough testing to determine which is the most
accurrate result, so for the time being, I recommend using 
calculate_latlong_distances.

'''

import utm
import geopy.distance
import math

def to_utm_list(latlong_list):
	'''
	This function converts a pair of latitude, longitude values, stored
	in a tuple, into the UTM Coordinate System.

	Input: List of tuples containing latlong coordinates

	Output: List of tuples containing UTM Coordinates. These UTM
	coordinates are in the form (EASTING, NORTHING, ZONE NUMBER, ZONE LETTER),
	but the ZONE NUMBER used for all given points is the same one that was
	used for the first one.
	'''

	# Empty list of UTM coordinates
	utm_list = []

	# Get the lattitude and longitude of the first point
	lat1 = latlong_list[0][0]
	lon1 = latlong_list[0][1]
	
	# Convert the first point to UTM and store its ZONE MUMBER
	fixed_zone_num = utm.from_latlon(lat1, lon1)[2]

	# Iterate through the coordinate list and convert everything into UTM
	for i in latlong_list:

		# Extract latitude and longitude
		lat = i[0]
		lon = i[1]

		utm_list.append(utm.from_latlon(lat, lon, force_zone_number = fixed_zone_num))

	# Return the created UTM list
	return utm_list


def calculate_utm_distances(utm_list):
	'''
	This function calculates the distance between each pair of UTM
	coordinate points by using the Pythagorean Theorem, and returns the
	distances in a list.

	Input: A list of (EASTING, NORTHING, ZONE NUMBER, ZONE LETTER) tuples
	(As used in the utm module)

	Output: A list of values, in meters, representing the distance between
	each pair of points.
	'''

	# Empty list of distances: Value at index n holds the distance between
	# point n and point n + 1
	utm_distance_list = []

	for i in range(len(utm_list) - 1):

		# Get each "triangle side" to use with the Pythagorean Theorem
		a = abs(utm_list[i][0] - utm_list[i+1][0])
		b = abs(utm_list[i][1] - utm_list[i+1][1])

		# Make the pythagorean calculation, return the result
		utm_distance_list.append(math.sqrt(math.pow(a, 2) + math.pow(b, 2)))

	return utm_distance_list


def calculate_latlong_distances(latlong_list):
	'''
	This function calculates the distance between each pair of points
	using the geopy.distance module, converted to meters.

	Input: A list of point coordinates in the form longitude/lattitude

	Output: A list of values, in meters, representing the distance between
	each pair of points.
	'''

	# Empty list of distances: Value at index n holds the distance between
	# point n and point n + 1
	latlong_distance_list = []

	for i in range(len(latlong_list) - 1):

		p1 = latlong_list[i]
		p2 = latlong_list[i+1]

		# Get each "triangle side" to use with the Pythagorean Theorem
		latlong_distance_list.append(geopy.distance.distance(p1, p2).km * 1000)

	return latlong_distance_list


def main:
	# Main function that will do a thing
	# Or not, it may not even exist. Depends.

if __name__ == '__main__':
	main()
