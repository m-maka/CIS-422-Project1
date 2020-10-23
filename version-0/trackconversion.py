'''
NOTE: This file was used in a previous version of the application.
I have decided to include it in case it helps future developers by
giving an idea of what we were trying to do. It is a raw file.

Authors: Max Aguirre, Brandon Bower, Mapuana Maka

This file contains functions that can convert pairs of lattitude and
longitude values into the UTM Coordinate System. It also calculates 
the distance between UTM points.

The first two methods, to_utm_list and calculate_utm_distances, take
a list of latlong and UTM coordinates, respectively. They then output
a list of UTM coordinates and a list of distanes between points, respectively.

The last two methods, to_utm and calculate_utm_distance, take an individual
latlong point and a pair of UTM points, respectively. They then output the
converted UTM coordinate and the distance between the two points, respectively.

'''

import utm
import geopy.distance
import math

import turntest

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
	latlong_distance_list = []

	for i in range(len(latlong_list) - 1):

		p1 = latlong_list[i]
		p2 = latlong_list[i+1]

		# Get each "triangle side" to use with the Pythagorean Theorem
		latlong_distance_list.append(geopy.distance.distance(p1, p2).km * 1000)

	return latlong_distance_list


def to_utm(coordinate):
	'''
	This function converts a pair of latitude, longitude values, stored
	in a tuple, into the UTM Coordinate System.

	Input: Tuple containing latitude, longitude values
	
	Output: Tuple of UTM coordinates in the form (EASTING, NORTHING, 
	ZONE NUMBER, ZONE LETTER)
	'''

	lat = coordinate[0]
	lon = coordinate[1]

	return utm.from_latlon(lat, lon)


def calculate_utm_distance(p1, p2):
	'''
	This function calculates the distance between two UTM
	coordinate points by using the Pythagorean Theorem.

	Input: A (EASTING, NORTHING, ZONE NUMBER, ZONE LETTER) tuple
	(As used in the utm module)

	Output: A value, in meters, representing the distance between
	the two points.

	Notes: At the moment, first it checks if the two points are in the
	same zone. If they are, the calculation takes place. If they aren't,
	it prints a message saying that the zones are different, and returns 0.
	'''

	# TODO: See Notes.

	# Check if both points are in the same UTM Zone
	#if p1[2] == p2[2] and p1[3] == p2[3]:
	if p1[2] == p2[2]:

		# Get each "triangle side" to use with the Pythagorean Theorem
		a = abs(p1[0] - p2[0])
		b = abs(p1[1] - p2[1])

		# Make the pythagorean calculation, return the result
		return math.sqrt(math.pow(a, 2) + math.pow(b, 2))
	
	else:
		print("Does not support multiple UTM zones at this time")
		return 0

def calculate_latlong_distance(p1, p2):
	'''
	This function calculates the distance between two lat/long
	coordinate points, in meters, by using geopy to get the
	distance in Km, then converts it to meters.

	Input: Two latlong coordinate tuples; the points.

	Output: A value, in meters, representing the distance between
	the two points.
	'''

	return geopy.distance.distance(p1, p2).km * 1000


def main():
	# Main function that was being used for testing

	#Latlong list
	latlong_track = [(46.57608333, 8.89241667), (46.57619444, 8.89252778), (46.57641667, 8.89266667), (46.5765, 8.89280556), (46.57638889, 8.89302778), (46.57652778, 8.89322222), (46.57661111, 8.89344444)]

	utm_track = to_utm_list(latlong_track)

	utm_dist_list = calculate_utm_distances(utm_track)

	print(utm_dist_list)

	latlong_dist_list = calculate_latlong_distances(latlong_track)

	print(latlong_dist_list)

	turntest.find_turn_direction()

	#x = -0.174943
	#y = -78.454952

	#x = 39.328147
	#y = -120.184061

	#x = 44.058069
	#y = -122.444118

	#x = 47.252812
	#y = 123

	#p1 = to_utm((x, y))
	#print(p1)

	#x2 = 1.205884
	#y2 = -77.286000

	#x2 = 39.529866 
	#y2 = -119.814250

	#x2 = 48.751905
	#y2 = -122.478819

	#x2 = 44.060004
	#y2 = -123.067299


	#p2 = to_utm((x2, y2))
	#print(p2)

	#print "Distance using coordinates: ", calculate_latlong_distance((x, y), (x2, y2))
	#print "Distance using UTM: ", calculate_utm_distance(p1, p2)


if __name__ == '__main__':
	main()
