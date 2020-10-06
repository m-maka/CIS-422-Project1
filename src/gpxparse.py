'''
Authors: Brandon Bower along with Max Aguirre and Mapuana Maka

gpx reading code from: https://pypi.org/project/gpxpy/

This file contains all functions related to reading, and obtaining information
from, a GPX file in order to reverse geocode a route.
'''

import gpxpy
#import gpxpy.gpx

def read(file):
    '''
    takes in a path to a gpx file in the form of a string,
    opens and reads the gpx file,
    and exports the relevant information.
    '''
    gpx_file = open(file ,'r')

    gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                print(f'Point at ({point.latitude}, {point.longitude}) -> {point.elevation}')
    return

def main():
    read('09_27_20.gpx')

if __name__ == '__main__':
    main()
    
