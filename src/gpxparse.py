'''
Authors: Brandon Bower along with Max Aguirre and Mapuana Maka

gpx reading code from: https://pypi.org/project/gpxpy/

This file contains all functions related to reading, and obtaining information
from, a GPX file in order to reverse geocode a route.
'''

import gpxpy

def read(file):
    '''
    takes in a path to a gpx file in the form of a string,
    opens and reads the gpx file,
    and exports the relevant information.
    '''
    with open(file ,'r') as gpx_file:

        gpx = gpxpy.parse(gpx_file)
        gpx.simplify()

        latlongs = []

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    latlongs.append((point.latitude, point.longitude))
    print(latlongs)
    return latlongs

def main():
    read('small.gpx')

if __name__ == '__main__':
    main()
    
