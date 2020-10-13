'''
Authors: Max Aguirre, Brandon Bower, Mapuana Maka

This file converts pairs of lattitude and longitude values into the UTM 
Coordinate System. It also calculates the distance between UTM points.

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


def main:
	# Main function that will do a thing
	# Or not, it may not even exist. Depends.

if __name__ == '__main__':
	main()
	