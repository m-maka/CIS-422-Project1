'''
Authors: Max Aguirre, Brandon Bower, Mapuana Maka

This file converts pairs of lattitude and longitude values into the UTM 
Coordinate System. It also calculates the distance between UTM points.

'''

import utm
import geopy.distance

def to_utm(coordinate):
	'''
	This function converts a pair of latitude, longitude values, stored
	in a tuple, into the UTM Coordinate System.

	Takes in a tuple of values
	Returns a tuple of UTM coordinates
	'''

	lat = coordinate[0]
	lon = coordinate[1]

	return utm.from_latlon(lat, lon)


def calculate_utm_distance(p1, p2):
	'''
	This function calculates the distance between two UTM
	coordinate points.
	'''


def calculate_latlong_distance(p1, p2):
	'''
	This function calculates the distance between two lat/long
	coordinate points, in meters
	'''

	return geopy.distance.distance(p1, p2).km * 1000


def main:
	# Main function that will do a thing
	# Or not, it may not even exist. Depends.

if __name__ == '__main__':
	main()

